const $api = $('api');
url = $api.attr('href-paginate')



window.onload = function(){
  fetch('http://localhost:5000/movies/?limit=2&offset=0')

    .then((response)=>{
      return response.json();
      alert(url);
    })
    .then((data)=>{
      for(let i = 1; i<=data.page_count; i++){
          const pageItem = document.createElement("li"); 
          pageItem.innerText = i;
          pageContainer.appendChild(pageItem)}
      getMovies(data.movies)
    })
}

function getMovies(movies){
  const moviesCont = document.querySelector(".movies")
  moviesCont.innerHTML = ''
  movies.forEach(item => {
    moviesCont.insertAdjacentHTML("beforeend",
    `<div class="movie__container">



    <p class="poster__movie"><img src="{{movie.img}}" alt="" class="movie__poster">

    <div class="movie__data">
        <div class="title__movie">${item.title}</div>

        <div class="genre">{%for genre in movie.genres%}<span>
                <a href="genre/{{genre.slug}}" class="btn-watch -g">{{genre.title}}</a>


            </span> {%endfor%}
        </div>
        <div class="description__movie"><span>
        ${item.descripion}</span>
        </div>

        <div>Year: <span>${item.year}</span></div>{%endif%}
        <div>Country: <span>${item.country}</span></div>{%endif%}

    </div>
    <a href="{{movie.slug}}" class="btn-watch">WATCH</a>
    <a href="{{movie.slug}}/edit" class="m-edit">edit</a>
    <a href="{{movie.slug}}/delete"class="m-delete" onclick="Delete(this)">delete</a>
    <a href="{{movie.slug}}/upload"class="m-upload">upload</a>

    </p>

</div>`)
  })
}

const pageContainer = document.querySelector('.pagesWrapper')
pageContainer.addEventListener('click', (e)=>{
  let activePage
  if(+e.target.innerHTML > 1){
    activePage = +e.target.innerHTML
  }
  else{
    activePage = +e.target.innerHTML - 1
  }
  fetch(`http://localhost:5000/movies/?limit=2&offset=${activePage}`)
  .then((response)=>{
    return response.json();
  })
  .then((data)=>{
    getMovies(data.movies)
  })
})

  