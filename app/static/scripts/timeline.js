const maxRotation = 4;
const minRotation = -4;

async function loadTimeline() {
  fetch('/api/timeline_post', {
    method: 'GET'
  })
  .then(response => response.json())
  .then((data) => {
    data['timeline_posts'].reverse().forEach(post => {
      addTimelinePost(post['name'], post['email'], post['content'], post['created_at']);
    });
  })
}

function addTimelinePost(name, email, content, date) {
  postCardDiv = document.createElement('div')
  postCardDiv.className = 'timeline-post'
  postCardDiv.style = `rotate: ${Math.floor(Math.random() * (maxRotation - minRotation + 1) + minRotation)}deg`

  postCardContentDiv = document.createElement('div')
  postCardContentDiv.className = 'timeline-post-content'

  postCardHeader = document.createElement('div')
  postCardHeader.className = 'timeline-post-header'

  postCardName = document.createElement('h3')
  postCardName.innerHTML = name
  postCardHeader.appendChild(postCardName)

  postCardEmail = document.createElement('h4')
  postCardEmail.innerHTML = `- ${email}`
  postCardHeader.appendChild(postCardEmail)

  postCardContentDiv.appendChild(postCardHeader)

  postCardDate = document.createElement('h4')
  postCardDate.innerHTML = date
  postCardDate.className = 'timeline-post-date'
  postCardContentDiv.appendChild(postCardDate)

  postCardContent = document.createElement('p')
  postCardContent.innerHTML = content
  postCardContentDiv.appendChild(postCardContent)

  postCardDiv.appendChild(postCardContentDiv)

  timelineDiv = document.getElementsByClassName('timeline-container')[0]
  timelineDiv.insertBefore(postCardDiv, timelineDiv.firstChild)
}

document.addEventListener('DOMContentLoaded', function() {
  loadTimeline();

  const form = document.getElementsByClassName('post-form')[0];

  form.addEventListener('submit', function(e) {
    e.preventDefault();
    const formData = new FormData(form);

    fetch('/api/timeline_post', {
      method: 'POST',
      body: formData
    })
    .then(response => response.json())
    .then((data) => {
      addTimelinePost(data['name'], data['email'], data['content'], data['created_at']);

      document.getElementById('form-name').value = '';
      document.getElementById('form-email').value = '';
      document.getElementById('form-content').value = '';
    })
  });
});