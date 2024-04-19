document.addEventListener('DOMContentLoaded', ()=>{
    document.querySelector('#edit').addEventListener('click', () => editar());
    
    document.querySelector('#voltar').addEventListener('click', () => index());

    document.querySelector('#prof_materia_add').addEventListener('click', (event) => {
        event.preventDefault();
        add_prof();
    });

    document.querySelector('#prof_materia_del').addEventListener('click', (event) => {
        event.preventDefault();
        del_prof();
    });

    

    index();
});

function limpa(){
    var divs = document.getElementsByTagName("div");
    for (var i = 0; i < divs.length; i++) {
        divs[i].style.display = 'none';
    }
}

function index(){
    limpa()
    document.querySelector('#conteudo').style.display = 'block';
}

function editar(){
    document.querySelector('#editar').style.display = 'block';
    document.querySelector('#conteudo').style.display = 'none';
}


function del_prof(){
    document.querySelector('#del_prof').style.display = 'block';
    document.querySelector('#add_prof').style.display = 'none';
}

function add_prof(){
    document.querySelector('#del_prof').style.display = 'none';
    document.querySelector('#add_prof').style.display = 'block';
    
}