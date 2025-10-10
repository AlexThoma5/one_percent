const editButtons = document.getElementsByClassName("btn-edit");
const editLogForm = document.getElementById("editLogForm");
const editModal= document.getElementById("editLogModal");

// Get editLog bootstrap modal
const newEditModal = new bootstrap.Modal(editModal);

/**
* Initialises edit functionality for the provided edit buttons.
* 
* For each button in the `editButtons` collection:
* - Retrieves the associated log's ID upon click.
* - Fetches the content of the corresponding log.
* - Fetches the input fields from the edit modal.
* - Populates the `logModalTitle` and 'logModalText' input fields with the log's content for editing.
* - Sets the form's action attribute to the `edit_log/{logId}/` endpoint.
* - Shows the new modal with fields populated.
*/
for (let button of editButtons) {
  button.addEventListener("click", (e) => {
    let logId = e.currentTarget.getAttribute("log_id");
    let logTitle = document.getElementById(`logTitle${logId}`).innerText;
    let logContent = document.getElementById(`log${logId}`).innerText;

    // Find the input fields inside the edit modal only
    let logModalText = editModal.querySelector("#id_content");
    let logModalTitle = editModal.querySelector("#id_title");

    // Fill the form fields
    logModalText.value = logContent;
    logModalTitle.value = logTitle;
    editLogForm.setAttribute("action", `edit_log/${logId}/`);

    // Show modal with content
    newEditModal.show()
  });
}
