function deleteNote(noteId) {
  // calls the delete note endpoint
  fetch("/delete-note", {
    method: "POST",
    body: JSON.stringify({ noteId: noteId }),
  }).then((_res) => {
    // reloads the page data
    window.location.href = "/";
  });
}
