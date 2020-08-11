console.log("Show_city")

const showForm = document.querySelector('.show-form');
const deleteBtns = document.querySelectorAll('#delete-btn');
const deleteAction = document.getElementById('delete-action');
const cancelAction = document.getElementById('cancel-action');

let postId, cityid, page;

deleteBtns.forEach(btn => btn.addEventListener('click', e => {
    showForm.hidden = true;
    cityid = btn.dataset.cityid
    postid = btn.dataset.postid
    page = btn.dataset.page
    dialogueContainer.classList.remove('hidden')
    deleteModal.hidden = false;
}))

cancelAction.addEventListener('click', e => {
    dialogueContainer.classList.add('hidden')
    showForm.hidden = false;
    deleteModal.hidden = true;
})

deleteAction.addEventListener('click', e => {
    dialogueContainer.classList.add('hidden')
    deleteModal.hidden = true;
    showForm.hidden = false;
    if (page === 'profile') {
        window.location.href = `/accounts/profile/${postid}/deletepost/`
    } else {
        window.location.href = `/cities/${cityid}/deletepost/${postid}/`
    }
})