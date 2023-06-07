document.addEventListener('DOMContentLoaded', function() {

  // Use buttons to toggle between views
  document.querySelector('#inbox').addEventListener('click', () => load_mailbox('inbox'));
  document.querySelector('#sent').addEventListener('click', () => load_mailbox('sent'));
  document.querySelector('#archived').addEventListener('click', () => load_mailbox('archive'));
  document.querySelector('#compose').addEventListener('click', compose_email);

  //when submit button is pressed in the compose form
  document.querySelector('#compose-form').onsubmit = () => {
        const recipients = document.querySelector('#compose-recipients').value;
        const subject = document.querySelector('#compose-subject').value;
        const body = document.querySelector('#compose-body').value;

        fetch('/emails', {
            method: 'POST', 
            body: JSON.stringify({
              recipients : recipients,
              subject: subject,
              body: body
            })
        })
        .then(response => response.json())
        .then(data => {
              console.log(data);
              load_mailbox('sent');
        })
        .catch(error => {
          console.log(error);
        })   

        return false;
  }

  // By default, load the inbox
  load_mailbox('inbox');
});

function compose_email() {

  // Show compose view and hide other views
  document.querySelector('#emails-view').style.display = 'none';
  document.querySelector('#compose-view').style.display = 'block';

  // Clear out composition fields
  document.querySelector('#compose-recipients').value = '';
  document.querySelector('#compose-subject').value = '';
  document.querySelector('#compose-body').value = '';
}

function load_mailbox(mailbox) {
  
  // Show the mailbox and hide other views
  document.querySelector('#emails-view').style.display = 'block';
  document.querySelector('#compose-view').style.display = 'none';

  fetch(`emails/${mailbox}`)
  .then(response => response.json())
  .then(data => {
    console.log(data);
    data.forEach(element => {
      //more styling can be added here by creating more elements and styling them
        const div = document.createElement('div');
        div.style.border = 'solid';
        div.style.margin = '5px';
        if(element.read){
          div.style.backgroundColor = 'grey';
        }
        div.innerHTML = `${element.sender}  ${element.subject}  ${element.timestamp}`;
        document.querySelector('#emails-view').appendChild(div); 
    });
    
    
  });

  // Show the mailbox name
  document.querySelector('#emails-view').innerHTML = `<h3>${mailbox.charAt(0).toUpperCase() + mailbox.slice(1)}</h3>`;
}