console.log("WayFAYer")

closeBox = document.querySelector('.close-box');
dialogueContainer = document.querySelector('.dialogueContainer')

closeBox.addEventListener('click', e => {
    dialogueContainer.classList.add('hidden')
})
