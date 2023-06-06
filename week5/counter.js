

if(!localStorage.getItem('counter')){
    localStorage.setItem('counter', 0);
}

function increment() {
    let counter = localStorage.getItem('counter');
    counter++;
    localStorage.setItem('counter', counter);
    document.querySelector('div').innerHTML = `Count: ${counter}`;
    }

document.addEventListener('DOMContentLoaded', function(){
    document.querySelector('div').innerHTML = `Count: ${localStorage.getItem('counter')}`;
    document.querySelector('button').addEventListener('click', increment);
});