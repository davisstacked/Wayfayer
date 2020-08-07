console.log("WayFAYer")

const closeBox = document.querySelector('.close-box') || null;
const dialogueContainer = document.querySelector('.dialogueContainer') || null
const profileCity = document.querySelectorAll('.profile-city') || null
const profilePost = document.querySelectorAll('.profile-post') || null
const cities = document.querySelector('.cities-click') || null // profile and show-city pages
const postHeader = document.querySelector('.profile-post-header') || null // profile and show-city pages
let count = 0;

if (cities !== null && postHeader !== null ) {
    count = 0;
    profilePost.forEach(post => {
        post.hidden = false;
        count++
    })

    postHeader.innerText = `Posts (${count})`
    cities.addEventListener('click', e => {
        profileCity.forEach(city => city.style.background = 'seashell')
        count = 0;
        profilePost.forEach(post => {
            post.hidden = false;
            count++
        })
        postHeader.innerText = `Posts (${count})`
    })
}

if (profileCity !== null ) {
    profileCity.forEach(city => city.addEventListener('click', e => {
        profileCity.forEach(city => city.style.backgroundColor = 'seashell')
        city.style.backgroundColor = 'plum'
        const chosenCity = city.dataset.city
        count = 0;
        profilePost.forEach(post => {
            post.hidden = false;
            if (post.dataset.city !== chosenCity) {
                post.hidden = true
            } else {
                count++
            }
        })
        postHeader.innerText = `Posts (${count})`
    })
    )
}

if (closeBox !== null ) {
    closeBox.addEventListener('click', e => {
        dialogueContainer.classList.add('hidden')
        window.history.back()
    })
}

