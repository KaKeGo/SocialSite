
const postsBox = document.getElementById('post-box')
const spinnerBox = document.getElementById('post-spinner')
const loadMoreBut = document.getElementById('load-more')
const moreBox = document.getElementById('more-box')

const locationUrl = window.location.href

visible = 1

const getData = () => {
    $.ajax({
        type: 'GET',
        url: `/data/${visible}`,
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
                                <input class="form-control border-dark bord" placeholder="Write comment">
                                <hr/>
                            </div>
                        </div>
                        `
                })
            }, 100);
            console.log(response.size)
            if (response.size === 0){
                loadMoreBut.innerHTML =
                    `
                    <strong>Eny blog not added yet</strong>
                    `
            }
            else if (response.size <= visible){
                moreBox.classList.add('not-visible')
                loadMoreBut.innerHTML =
                    `
                    <strong>No more blogs</strong>
                    `
            }
        },
        error: function (error){
            console.log(error)
        }
    })
}

loadMoreBut.addEventListener('click', () =>{
    spinnerBox.classList.remove('not-visible')
    visible += 1
    getData()
})

getData()
