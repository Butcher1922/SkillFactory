const dataURL = "https://api.myjson.com/bins/jcmhn";
const field = ["var1", "var2", "var3", "var4", "var5", "var6", "speach"];

/*function getFormVal(){
    let obj = {};
    fields.forEach(function(field){
        obj[field] = $("input[name="]+field+"]")[0].value
    });
    return obj;
}*/

function getFormVal() {
	let formValues = $("form").serializeArray();
	let obj = {};
	for (let i = 0; i < formValues.length; i++) {
		obj[formValues[i]["name"]] = formValues[i]["value"];
	}
	return obj;
}

function handleButton(){
    $.getJSON(dataURL, handleData);
    $("form").hide();
    event.preventDefault();
}

function handleData(data){
    let message = "";

    let vals = getFormVal();
    
    data["text"].forEach(function(item){
        for (i in vals) {
            item = item.replace("{"+i+"}", vals[i]);
        }
        message = message + item + "<BR>";
    });
    
    $("div#content").html(message);
}

function init(){
    $("#button-fetch").click(handleButton);
}
$(document).ready(init);
