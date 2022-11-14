const message = document.querySelector("#message");
if (message) {
  message.classList.add("animate-open");
  setTimeout(() => {
    message.classList.add("animate-close");
  }, 6000);
  setTimeout(() => {
    message.remove();
  }, 10000);
}
