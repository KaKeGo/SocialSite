
const postBox = document.getElementById('post-box')
const postForm = document.getElementById('post-form')
const imgBox = document.getElementById('img-box')

const body = document.getElementById('id_body')
const image = document.getElementById('id_image')
const author = document.getElementById('id_author')

const url = ''


image.addEventListener('change', ()=>{
    const img_data = image.files[0]
    const url = URL.createObjectURL(img_data)
    imgBox.innerHTML = `<img src="${url}" width="100%">`
})

postForm.addEventListener('submit', e=>{
    e.preventDefault()

    const fd = new FormData()
    fd.append('csrfmiddlewaretoken', csrf[0].value)
    fd.append('name', body.value)
    fd.append('author', author.value)
    fd.append('image', image.files[0])

    $.ajax({
        type: 'POST',
        url: url,
        enctype: 'multipart/form-data',
        data: fd,
        success: function (response){
            const stext= `successfully created post`
            handleAlerts('success', stext)
            setTimeout(()=>{
                alertBox.innerHTML = ''
                imgBox.innerHTML = ''
                body.value = ''
                author.value = ''
                image.value = ''
                window.location.reload()
            }, 1000)
        },
        error: function (error){
            handleAlerts('danger', 'Ups something went wrong')
        },
        cache: false,
        contentType: false,
        processData: false,
    })
})
