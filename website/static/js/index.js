function delete_note(noteId) {
  fetch("/delete-note", {
    // calls the delete endpoint
    method: "POST",
    body: JSON.stringify({
      noteId: noteId,
    }).then((_res) => {
      // then reload the page to Home
      window.location.reload = "/";
    }),
  });
}
