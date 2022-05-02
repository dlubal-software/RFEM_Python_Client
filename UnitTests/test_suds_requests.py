#######################################################################
# THIS SOFTWARE IS PROVIDED BY THE AUTHOR ``AS IS'' AND ANY EXPRESS OR
# IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY DIRECT,
# INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
# (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
# SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION)
# HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT,
# STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING
# IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.
#
# Curtesy of https://github.com/armooo/suds_requests
# author: Jason Michalski
# email: armooo@armooo.net
# License: MIT
#######################################################################

import os
import sys
import mock
import pytest
import requests
import suds.transport
PROJECT_ROOT = os.path.abspath(os.path.join(
                  os.path.dirname(__file__),
                  os.pardir)
)
sys.path.append(PROJECT_ROOT)
import RFEM.suds_requests as suds_requests


def test_no_errors():
    m = mock.Mock(__name__='m')
    f = suds_requests.handle_errors(m)
    assert f() == m.return_value


def test_HTTPError():
    resp = mock.Mock(status_code=404,
                     content=b'File not found')
    m = mock.Mock(
        side_effect=requests.HTTPError(response=resp),
        __name__='m',
    )
    f = suds_requests.handle_errors(m)
    with pytest.raises(suds.transport.TransportError) as excinfo:
        f()
    assert excinfo.value.httpcode == 404
    assert excinfo.value.fp.read() == b'File not found'


def test_RequestException():
    m = mock.Mock(
        side_effect=requests.RequestException(),
        __name__='m',
    )
    f = suds_requests.handle_errors(m)
    with pytest.raises(suds.transport.TransportError) as excinfo:
        f()
    assert excinfo.value.httpcode == 000
    assert excinfo.value.fp.read().startswith(b'Traceback')

def test_open():
    session = mock.Mock()
    session.get.return_value.content = b'abc123'
    transport = suds_requests.RequestsTransport(session)
    request = suds.transport.Request('http://url')

    response = transport.open(request)

    assert response.read() == b'abc123'


def test_send():
    session = mock.Mock()
    session.post.return_value.content = b'abc123'
    session.post.return_value.headers = {
        1: 'A',
        2: 'B',
    }
    session.post.return_value.status_code = 200
    transport = suds_requests.RequestsTransport(session)
    request = suds.transport.Request(
        'http://url',
        'I AM SOAP! WHY AM I NOT CLEAN!!!',
    )
    request.headers = {
        'A': 1,
        'B': 2,
    }

    reply = transport.send(request)

    session.post.assert_called_with(
        'http://url',
        data='I AM SOAP! WHY AM I NOT CLEAN!!!',
        headers={
            'A': 1,
            'B': 2,
        },
    )
    assert reply.code == 200
    assert reply.headers == {
        1: 'A',
        2: 'B',
    }
    assert reply.message == b'abc123'