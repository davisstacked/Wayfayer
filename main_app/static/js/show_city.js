console.log("Show_city")

const deleteBtns = document.querySelectorAll('#delete-btn')
const deleteModal = document.querySelector('.delete-modal');
const deleteActioin = document.getElementById('delete-action')
const cancelActioin = document.getElementById('cancel-action')
// const dialogueContainer = document.querySelector('.dialogueContainer')
let postId, cityid;

deleteBtns.forEach(btn => btn.addEventListener('click', e => {
    // console.log(btn.dataset.postid);
    cityid = btn.dataset.cityid
    postid = btn.dataset.postid
    dialogueContainer.classList.remove('hidden')
    deleteModal.classList.remove('hidden');
}))

cancelActioin.addEventListener('click', e => {
    console.log("cancel action", cityid, postid)
    dialogueContainer.classList.add('hidden')
    deleteModal.classList.add('hidden');
})

deleteActioin.addEventListener('click', e => {
    console.log("delete action", cityid, postid)
    dialogueContainer.classList.add('hidden')
    deleteModal.classList.add('hidden');
    window.location.href = `/cities/${cityid}/deletepost/${postid}/`
})