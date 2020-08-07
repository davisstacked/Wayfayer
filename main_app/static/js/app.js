console.log("WayFAYer")

const closeBox = document.querySelector('.close-box');
const dialogueContainer = document.querySelector('.dialogueContainer')
const profileCity = document.querySelectorAll('.profile-city')
const profilePost = document.querySelectorAll('.profile-post')



closeBox.addEventListener('click', e => {
    dialogueContainer.classList.add('hidden')
    window.history.back()
})

profileCity.forEach(city => city.addEventListener('click', e => {
    profileCity.forEach(city => city.style.background = 'gray')
    city.style.background = 'orange'
    const chosenCity = city.dataset.city
    profilePost.forEach(post => {
        post.hidden = false;
        if (post.dataset.city !== chosenCity) {
            post.hidden = true
        }
    })
})
)