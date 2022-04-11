
const spinnerBox = document.getElementById('group-spinner')
const groupBox = document.getElementById('group-box')

const url = window.location.href

const getData = () => {
    $.ajax({
        'type': 'GET',
        'url': `/groups/data/`,
        success: function (response){
            console.log(response)
            const data = response.data
            setTimeout(() => {
                spinnerBox.classList.add('not-visible')
                console.log(data)
                data.forEach(el => {
                    groupBox.innerHTML +=
                        `
                        <div class="card-title p-2 mt-3 bg-dark bord nor-text">
                            <div class="display-inline">
                                <img class="avat mx-2 nor-text" src="${el.gavatar}">
                                <a class="lis-worlds" href="">${el.name}</a>
                            </div>
                            <hr/>
                            <div class="mx-2">
                                <p class="nor-text">${el.description}</p>
                            </div>
                            <hr/>
                            <div class="mx-2">
                                <p class="nor-text me-auto" href="">Members: ${el.total_members}</p>
                            </div>
                            <div class="text-center">
                                <a class="btn btn-primary" href="${url}${el.name.toLowerCase()}">Check</a>
                            </div>
                        </div>
                        `
                })
            }, 100)
        },
        error: function (error){
            console.log(error)
        }
    })
}

getData()
