
const avatarBox = document.getElementById('avatar-box')
const groupForm = document.getElementById('group-form')

const name = document.getElementById('id_name')
const gavatar = document.getElementById('id_gavatar')
const founder = document.getElementById('id_founder')
const description = document.getElementById('id_description')

const url = ''


gavatar.addEventListener('change', () => {
    const avatar_data = gavatar.files[0]
    const url = URL.createObjectURL(avatar_data)
    avatarBox.innerHTML = `<img src="${url}" width="100%">`
})

groupForm.addEventListener('submit', e => {
    e.preventDefault()

    const fd = new FormData()
    fd.append('csrfmiddlewaretoken', csrf[0].value)
    fd.append('founder', founder.value)
    fd.append('name', name.value)
    fd.append('description', description.value)
    fd.append('gavatar', gavatar.files[0])

    $.ajax({
        type: 'POST',
        url:url,
        enctype: 'multipart/form-data',
        data: fd,
        success: function (response){
            const stext = `successfully created post`
            handleAlerts('success', stext)
            setTimeout(function (){
                window.location.href = ''
            }, 2000)
        },
        error: function (error){
            handleAlerts('danger', 'Ups something went wrong')
        },
        cache: false,
        contentType: false,
        processData: false,
    })
})
