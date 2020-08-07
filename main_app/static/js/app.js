console.log("WayFAYer")

const closeBox = document.querySelector('.close-box');
const dialogueContainer = document.querySelector('.dialogueContainer')

closeBox.addEventListener('click', e => {
    dialogueContainer.classList.add('hidden')
    window.history.back()
})
