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

import functools
import requests
import suds.transport as transport
import traceback
from six import BytesIO

def handle_errors(f):
    @functools.wraps(f)
    def wrapper(*args, **kwargs):
        try:
            return f(*args, **kwargs)
        except requests.HTTPError as e:
            buf = BytesIO(e.response.content)
            raise transport.TransportError(
                'Error in requests\n' + traceback.format_exc(),
                e.response.status_code,
                buf,
            )
        except requests.RequestException:
            buf = BytesIO(traceback.format_exc().encode('utf-8'))
            raise transport.TransportError(
                'Error in requests\n' + traceback.format_exc(),
                000,
                buf,
            )
    return wrapper


class RequestsTransport(transport.Transport):
    def __init__(self, session=None):
        transport.Transport.__init__(self)
        self._session = session or requests.Session()

    @handle_errors
    def open(self, request):
        resp = self._session.get(request.url)
        resp.raise_for_status()
        return BytesIO(resp.content)

    @handle_errors
    def send(self, request):
        resp = self._session.post(
            request.url,
            data=request.message,
            headers=request.headers,
        )
        if resp.headers.get('content-type') not in ('text/xml',
                                                    'application/soap+xml'):
            resp.raise_for_status()
        return transport.Reply(
            resp.status_code,
            resp.headers,
            resp.content,
        )
