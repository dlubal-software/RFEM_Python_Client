function showPanel(){
	var framePanels = document.getElementsByTagName("iframe");
	var datalist = document.getElementById('filter');
	var searchField = document.getElementById('fl');
	var searchFieldTableName = searchField.value;
	for (let i = 0; i < datalist.options.length; i++) {
		if (searchFieldTableName == datalist.options[i].label){
			framePanels[i].style.display="block";
		}
		else{
			framePanels[i].style.display="none";
		}
	}
	searchField.blur();
};
function switchButtonDown(){
	var datalist = document.getElementById('filter');
	var searchField = document.getElementById('fl');
	var searchFieldTableName = searchField.value;
	var index = 0;
	for (let i = 0; i < datalist.options.length; i++) {
		if (searchFieldTableName == datalist.options[i].label){
			index = i;
			break;
		}
	}
	index = index - 1;
	index = Math.max(0, index);
	searchField.value = datalist.options[index].label;
	showPanel();
};
function switchButtonUp(){
	var datalist = document.getElementById('filter');
	var searchField = document.getElementById('fl');
	var searchFieldTableName = searchField.value;
	var index = 0;
	for (let i = 0; i < datalist.options.length; i++) {
		if (searchFieldTableName == datalist.options[i].label){
			index = i;
			break;
		}
	}
	index = index + 1
	index = Math.min(datalist.options.length-1, index);
	searchField.value = datalist.options[index].label;
	showPanel();
};
function updateProgressBar() {
	var filters = document.getElementById('filter').options.length;
	var pbv = document.getElementById('progressBar').value;
	document.getElementById('progressBar').value = Math.fround(pbv + 100/filters);
};
function atTheEnd(){
	var datalist = document.getElementById('filter');
	var searchField = document.getElementById('fl');
	searchField.value = datalist.options[0].label;
	//document.getElementById("progressBar").style.display="none";
	showPanel();
	document.getElementsByClassName("tabContainer")[0].style.visibility = 'visible';
};
