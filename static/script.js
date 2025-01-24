const socket = io();

const projname = window.projname;

const termout = document.getElementById('output');
const termin = document.getElementById('input');

terminalInput.addEventListener('keydown', (event) => {
  if (event.key === "Enter") {
    const command = termin.value;
    termin.value = '';
    appendToOutput(`$ ${command}`);
    socket.emit('execute', { projname: projname, command: command  });
  }
});

socket.on('output', (data) => {
  appendToOutput(data.output);
});

function appendToOutput(text) {
  terminalOutput.innerHTML += `<div>${text}</div>`;
  terminalOutput.scrollTop = terminalOutput.scrollHeight;
}
