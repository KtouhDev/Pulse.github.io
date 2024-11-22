function loadPosts() {

    const postsContainer = document.getElementById('feed');
    const posts = [
      {
        author: 'Иван Иванов',
        content: 'Привет, мир!',
        image: 'post-image.png'
      },
      {
        author: 'Мария Петрова',
        content: 'Сегодня отличная погода!',
        image: 'post-image2.png'
      }
    ];
  
    posts.forEach(post => {
      const postElement = document.createElement('div');
      postElement.classList.add('post');
      postElement.innerHTML = `
        <div class="user-info">
          <img src="${post.image}" alt="Аватар пользователя">
          <span class="username">${post.author}</span>
        </div>
        <div class="post-content">
          <p>${post.content}</p>
        </div>
      `;
      postsContainer.appendChild(postElement);
    });
  }
  
  // Вызываем функцию для загрузки постов при загрузке страницы
  window.onload = loadPosts;
  