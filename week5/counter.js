let counter = 0;
        function increment() {
            counter++;
            document.querySelector('div').innerHTML = `Count: ${counter}`;
            if (counter % 10 === 0){
                alert(`Count is now ${counter}!`);
            } 
        }

        document.addEventListener('DOMContentLoaded', function(){
            document.querySelector('button').addEventListener('click', increment);
        });