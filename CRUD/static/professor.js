document.addEventListener('DOMContentLoaded', ()=> {
    document.querySelector('#edit').addEventListener('click', () => editar());

    document.querySelector('#add_mat').addEventListener('click', (event) => {
        event.preventDefault();
        add_materias();
    });

    document.querySelector('#del_mat').addEventListener('click', (event) => {
        event.preventDefault();
        delete_materias();
    });

    document.querySelector('#voltar').addEventListener('click', () => index());
 

    index();
});

function limpa(){
    var divs = document.getElementsByTagName("div");
    for (var i = 0; i < divs.length; i++) {
        divs[i].style.display = 'none';
    }
}

function index(){
    limpa();
    document.querySelector('#editar').style.display = 'none';
    document.querySelector('#conteudo').style.display = 'block';
}

function editar(){
    document.querySelector('#editar').style.display = 'block';
    document.querySelector('#conteudo').style.display = 'none';

}


function add_materias(){
    document.querySelector('#add_materia').style.display = 'block';
    document.querySelector('#delete_materias').style.display = 'none';
}

function delete_materias(){
    document.querySelector('#delete_materias').style.display = 'block';
    document.querySelector('#add_materia').style.display = 'none';
}