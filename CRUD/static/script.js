document.addEventListener('DOMContentLoaded', ()=>{
    //por default
    index();
    document.querySelector('#alunos').addEventListener('click', () => alunos());
    document.querySelector('#professores').addEventListener('click', () => professores());
    document.querySelector('#cursos').addEventListener('click', () => cursos());
    document.querySelector('#materias').addEventListener('click', () => materias());
    
    var voltar = document.getElementsByClassName("voltar");
    for (var i = 0; i < voltar.length; i++) {
      voltar[i].addEventListener('click', () => index());
    }

    // BOTÕES ALUNOS
    document.querySelector('#botao_pc').addEventListener('click', () => show_pc());
    document.querySelector('#botao_add_al').addEventListener('click', () => add_aluno());
    document.querySelector('#botao_mostrar_al').addEventListener('click', () => mostrar_alunos());

    // BOTÕES CURSOS
    document.querySelector('#botao_mostrar_c').addEventListener('click', () => mostrar_cursos());
    document.querySelector('#botao_pc_curso').addEventListener('click', () => proc_curso());
    document.querySelector('#botao_add_c').addEventListener('click', () => add_cursos());

    // BOTÕES MATERIAS
    document.querySelector('#botao_mostrar_mat').addEventListener('click', () => mostrar_materias());
    document.querySelector('#botao_pc_mat').addEventListener('click', () => proc_materia());
    document.querySelector('#botao_add_mat').addEventListener('click', () => add_materia());


    // BOTÔES PROFESSORES
    
    document.querySelector('#botao_pc_prof').addEventListener('click', () => show_pc_prof());
    document.querySelector('#botao_mostrar_profs').addEventListener('click', () => mostrar_todos_profs());
    document.querySelector('#botao_cria_prof').addEventListener('click', () => cria_professores());
    
   


});

function limpa(){
    var divs = document.getElementsByTagName("div");
    for (var i = 0; i < divs.length; i++) {
        divs[i].style.display = 'none';
    }
}
function index(){
    limpa()
    document.querySelector('#buttons').style.display = 'block';

}

function alunos(title){
    document.querySelector('#div_alunos').style.display = 'block';
    document.querySelector('#buttons').style.display = 'none';

}

function add_prof(title){
 
    document.querySelector('#add').style.display = 'block';
    document.querySelector('#buttons').style.display = 'none';
}

// MAATERIAS

function materias(){

    document.querySelector('#div_materias').style.display = 'block';
    document.querySelector('#buttons').style.display = 'none';

}
function mostrar_materias(){
    document.querySelector('#mostrar_materias').style.display = 'block';
    document.querySelector('#buttons').style.display = 'none';
}

function proc_materia(){
    document.querySelector('#proc_materias').style.display = 'block';
    document.querySelector('#buttons').style.display = 'none';
}
function add_materia(){
    document.querySelector('#add_materias').style.display = 'block';
    document.querySelector('#buttons').style.display = 'none';
}
// ALUNOS

function show_pc(){
    document.querySelector('#pc').style.display = 'block';
}

function add_aluno(title){

    document.querySelector('#add_al').style.display = 'block';
    document.querySelector('#buttons').style.display = 'none';
}

function mostrar_alunos(title){

    document.querySelector('#mostrar_al').style.display = 'block';
    document.querySelector('#buttons').style.display = 'none';
}

// CURSOS
function cursos(){
    document.querySelector('#div_cursos').style.display = 'block';
    document.querySelector('#buttons').style.display = 'none';

}

function mostrar_cursos(title){

    document.querySelector('#mostrar_cursos').style.display = 'block';
    document.querySelector('#buttons').style.display = 'none';
}

function proc_curso(){
    document.querySelector('#proc_curso').style.display = 'block';
    document.querySelector('#buttons').style.display = 'none';
}

function add_cursos(){
    document.querySelector('#add_curso').style.display = 'block';
    document.querySelector('#buttons').style.display = 'none';
}


// PROFESSORES

function professores(title){

    document.querySelector('#div_professores').style.display = 'block';
    document.querySelector('#buttons').style.display = 'none';
}

function cria_professores(title){
    document.querySelector('#cria_prof').style.display = 'block';
    document.querySelector('#buttons').style.display = 'none';
}

function show_pc_prof(){
    document.querySelector('#pc_prof').style.display = 'block';
}

function mostrar_todos_profs(){
    document.querySelector('#mostrar_prof').style.display = 'block';
}
