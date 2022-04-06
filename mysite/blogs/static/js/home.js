
const postsBox = document.getElementById('post-box')
const spinnerBox = document.getElementById('post-spinner')

const locationUrl = window.location.href

const getData = () => {
    $.ajax({
        type: 'GET',
        url: '/data/',
        success: function (response){
            console.log(response)
            const data = response.data
            setTimeout(() =>{
                spinnerBox.classList.add('not-visible')
                data.forEach(el => {
                    postsBox.innerHTML +=
                        `
                        <div class="card-title p-2 mt-3 bg-dark bord">
                            <div class="display-inline">
                                <img class="avat mx-2" src="${el.avatar}"><a class="lis-worlds" href="${locationUrl}accounts/profile/${el.author.toLowerCase()}">${el.author}</a>
                            </div>
                            <hr/>
                            <div class="">${el.body}</div>
                            <div class="mt-2">
                                <img class="emage" src="${el.image}">
                            </div>
                            <div class="mt-3">
                                <a class="small nor-text">Create: ${el.create_on} </a> <a class="ms-2 like"><i class="fa-solid fa-heart big"></a></i><a class="me-auto nor-text"> ${el.total_likes}</a>
                                <hr/>
                            </div>
                        </div>
                        `
                })
            }, 100);
        },
        error: function (error){
            console.log(error)
        }
    })
}

getData()
