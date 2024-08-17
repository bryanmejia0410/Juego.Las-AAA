let score = 0;

document.querySelectorAll('.item').forEach(item => {
    item.addEventListener('dragstart', dragStart);
});

document.querySelectorAll('.bin').forEach(bin => {
    bin.addEventListener('dragover', dragOver);
    bin.addEventListener('drop', dropItem);
});

function dragStart(event) {
    event.dataTransfer.setData('text/plain', event.target.id);
}

function dragOver(event) {
    event.preventDefault();
}

function dropItem(event) {
    const id = event.dataTransfer.getData('text');
    const item = document.getElementById(id);
    const bin = event.target;

    if (isCorrectBin(item, bin)) {
        bin.appendChild(item);
        score += 100;
        updateScore();
    } else {
        alert('¡Clasificación incorrecta!');
    }
}

function isCorrectBin(item, bin) {
    const itemId = item.id;
    const binId = bin.id;

    if (itemId.includes('newspaper') && binId === 'bin-paper') {
        return true;
    } else if (itemId.includes('bottle') && binId === 'bin-glass') {
        return true;
    } else if (itemId.includes('bag') && binId === 'bin-plastic') {
        return true;
    } else if (itemId.includes('can') && binId === 'bin-metal') {
        return true;
    } else if (itemId.includes('fruit-peel') && binId === 'bin-organic') {
        return true;
    } else if (itemId.includes('battery') && binId === 'bin-hazardous') {
        return true;
    }
    return false;
}

function GameOver (){
 if (isCorrectBin){
     return alert("¡Felicidades Haz Completado El Juego Correctamente!")
} else {
     return false; }


function updateScore() {
    document.getElementById('score').textContent = `Puntuación: ${score}`;
}
