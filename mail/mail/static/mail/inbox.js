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
  document.querySelector('#mail-view').style.display = 'none';

  // Clear out composition fields
  document.querySelector('#compose-recipients').value = '';
  document.querySelector('#compose-subject').value = '';
  document.querySelector('#compose-body').value = '';
}

function archive_switch(mail_id, archive_status){
  fetch(`/emails/${mail_id}`, {
    method: 'PUT',
    body: JSON.stringify({
      archived: !archive_status
    })
  });
  load_mailbox('inbox');
 
}




//loading a unique mail
function load_mail(mail_id, mailbox) {
  //making other components invisible
  document.querySelector('#emails-view').style.display = 'none';
  document.querySelector('#compose-view').style.display = 'none';
  document.querySelector('#mail-view').style.display = 'block';
  console.log(mail_id);

  //sending request to get the email data
  fetch(`/emails/${mail_id}`)
  .then(result => result.json())
  .then(data => {
        //updating the read attribute
        fetch(`/emails/${mail_id}`,{
          method: 'PUT', 
          body: JSON.stringify({
            'read': true
          }) 
        });
        //creating a new div to contain the data and filling it
        div = document.createElement('div')
        div.innerHTML = `<div><b>Sender: </b>${data.sender}</div>
                          <div><b>Recipients: </b>${data.recipients}</div>
                          <div><b>Subject: </b>${data.subject}</div> 
                          <div><b>Time Stamp: </b>${data.timestamp}</div> 
                          <div><b>Body: </b></div> 
                          <div>${data.body}</div>`;
        if(mailbox === 'inbox' || mailbox === 'archive'){
          button = document.createElement('button');
          if(!data.archived){
            button.innerHTML = 'Archive';
          } else {
            button.innerHTML = 'Unarchive';
          }
          button.addEventListener('click', function(){
            archive_switch(data.id, data.archived);
          })
          div.append(button)
        }
        replybtn = document.createElement('button');
        replybtn.innerHTML = 'Reply';
        replybtn.style.margin = '10px';
        replybtn.addEventListener('click', function(){
            compose_email();
            document.querySelector('#compose-recipients').value = data.sender;
            document.querySelector('#compose-subject').value = `Re: ${data.subject}`;
            document.querySelector('#compose-body').value = `On ${data.timestamp} ${data.sender} wrote: ${data.body}\n-->`;

        })
        div.append(replybtn);
        
        document.querySelector('#mail-view').append(div);
  });
}





function load_mailbox(mailbox) {
  // Show the mailbox and hide other views
  document.querySelector('#emails-view').style.display = 'block';
  document.querySelector('#compose-view').style.display = 'none';
  //hiding mailview and deleting any potential data inside it
  const mailview = document.querySelector('#mail-view');
  mailview.style.display = 'none';
  if(mailview.hasChildNodes()){
    mailview.removeChild(mailview.firstChild)
  }

//sending request to the API to receive all emails in the inbox
  fetch(`emails/${mailbox}`)
  .then(response => response.json())
  .then(data => {
    console.log(data);
    data.forEach(element => {
        //creating a new div for each found email and styling it 
        const div = document.createElement('div');
        div.style.border = 'solid';
        div.style.margin = '5px';
        if(element.read){
          div.style.backgroundColor = 'grey';
        }
        div.innerHTML = `<b>${element.sender}</b>  ${element.subject} <div style="text-align: right;">${element.timestamp}</div>`;
        //adding an event listener to each email to acces their unique page later
        div.addEventListener('click', function(){
            load_mail(element.id, mailbox); 
        });
        document.querySelector('#emails-view').append(div); 
    });
    
    
  });

  // Show the mailbox name
  document.querySelector('#emails-view').innerHTML = `<h3>${mailbox.charAt(0).toUpperCase() + mailbox.slice(1)}</h3>`;
}