
const postsBox = document.getElementById('post-box')
const spinnerBox = document.getElementById('post-spinner')
const loadMoreBut = document.getElementById('load-more')
const moreBox = document.getElementById('more-box')

const locationUrl = window.location.href

const likePosts = () =>{
    const likeForm = [...document.getElementsByClassName('like-form')]
    likeForm.forEach(form => form.addEventListener('submit', e =>{
        e.preventDefault()
        const clickerID = e.target.getAttribute('data-form-id')
        const clickedBtn = document.getElementById(`like-${clickerID}`)

        $.ajax({
            type: 'POST',
            url: '/like/',
            data: {
                'csrfmiddlewaretoken': csrftoken,
                'pk': clickerID
            },
            success: function (response){
                clickedBtn.innerText = response.liked ? `Like: ${response.count}`:`Unlike: ${response.count}`
            },
            error: function (error){
                console.log(error)
            }
        })
    }))
}

visible = 4

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
                            <form class="mt-3 like-form" method="post" data-form-id="${el.id}">
                                <a class="small nor-text" >Create: ${el.create_on} 
                                </a><button class="btn btn-success small btn-sm" type="submit" name="liked" id="like-${el.id}"> ${el.liked ? `Like: ${el.count}`: `Unlike: ${el.count}`}</button>
                                <a class="me-auto nor-text"></a>
                                <hr/>
                                <input class="form-control border-dark bord" placeholder="Write comment">
                                <hr/>
                            </form>
                        </div>
                        `
                })
                likePosts()
            }, 100);
            console.log(response.size)
            if (response.size === 0){
                moreBox.innerHTML =
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
    visible += 4
    getData()
})

getData()
