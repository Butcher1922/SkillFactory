const header = new Headers({
	'Access-Control-Allow-Credentials': true, 
  'Access-Control-Allow-Origin': '*'
})

const url = new URL('https://sf-pyw.mosyag.in/sse/vote/stats')

const ES = new EventSource(url, header);

const progress_1 = document.querySelector('#cat');
const progress_2 = document.querySelector('#parrot');
const progress_3 = document.querySelector('#dog');

ES.onopen = event => {
  console.log(event)
}

ES.onerror = error => {
  ES.readyState ? console.error("EventSource failed: ", error) : null;
};

ES.onmessage = ({data}) => {
    let get_data = JSON.parse(data)
    progress_1.style.cssText=`width: ${Math.round((get_data.cats * 100) / (get_data.cats + get_data.parrots + get_data.dogs))}%;`;
    progress_1.textContent = `${get_data.cats}`;
    progress_2.style.cssText=`width: ${Math.round((get_data.parrots * 100) / (get_data.cats + get_data.parrots + get_data.dogs))}%;`;
    progress_2.textContent = `${get_data.parrots}`;
    progress_3.style.cssText=`width: ${Math.round((get_data.dogs * 100) / (get_data.cats + get_data.parrots + get_data.dogs))}%;`;
    progress_3.textContent = `${get_data.dogs}`;
    //ES.close();
}

function voite(animal){
    let a = new XMLHttpRequest();
    a.open("POST","https://sf-pyw.mosyag.in/sse/vote/"+animal);
    a.send();
    document.querySelector('#results').style.cssText='display:;';
    document.querySelector('#voite').style.cssText='display: none;';
}
