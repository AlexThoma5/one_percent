const editButtons = document.getElementsByClassName("btn-edit");
const editLogForm = document.getElementById("editLogForm");
const editModal = document.getElementById("editLogModal");
const newEditModal = new bootstrap.Modal(editModal);

const deleteModal = new bootstrap.Modal(document.getElementById("deleteModal"));
const deleteButtons = document.getElementsByClassName("btn-delete");
const deleteConfirm = document.getElementById("deleteConfirm");

const alerts = document.querySelectorAll(".alert");

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
    let logId = e.currentTarget.getAttribute("data-log_id");
    let logTitle = document.getElementById(`logTitle${logId}`).innerText;
    let logContent = document.getElementById(`log${logId}`).innerText;

    // Find the input fields inside the edit modal only
    let logModalText = editModal.querySelector("#id_edit-content");
    let logModalTitle = editModal.querySelector("#id_edit-title");

    // Fill the form fields
    logModalText.value = logContent;
    logModalTitle.value = logTitle;
    editLogForm.setAttribute("action", `edit_log/${logId}/`);

    // Show modal with content
    newEditModal.show();
  });
}

/**
 * Initializes deletion functionality for the provided delete buttons.
 *
 * For each button in the `deleteButtons` collection:
 * - Retrieves the associated log's ID upon click.
 * - Updates the `deleteConfirm` link's href to point to the
 * deletion endpoint for the specific comment.
 * - Displays a confirmation modal (`deleteModal`) to prompt
 * the user for confirmation before deletion.
 */
for (let button of deleteButtons) {
  button.addEventListener("click", (e) => {
    let logId = e.currentTarget.getAttribute("data-log_id");
    deleteConfirm.href = `delete_log/${logId}`;
    deleteModal.show();
  });
}

/**
 * Iterates over all the elements with the 'alert' class,
 * waits 4 seconds and then automatically closes them
 * if they are still visible.
 */

alerts.forEach((alert) => {
  setTimeout(() => {
    if (alert.classList.contains("show")) {
      bootstrap.Alert.getOrCreateInstance(alert).close();
    }
  }, 4000);
});
