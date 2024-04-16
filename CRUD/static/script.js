document.addEventListener('DOMContentLoaded', ()=>{
    document.querySelector('#alunos').addEventListener('click', () => alunos());
    document.querySelector('#add_aluno').addEventListener('click', () => add_aluno('Adiciona alunos'));
    document.querySelector('#update').addEventListener('click', () => atualiza('update'));
    document.querySelector('#delete').addEventListener('click', () => deleta('delete'));
    
    var voltar = document.getElementsByClassName("voltar");
    for (var i = 0; i < voltar.length; i++) {
      voltar[i].addEventListener('click', () => index());
    }

    // botões alunos
    document.querySelector('#botao_pc').addEventListener('click', () => show_pc());

    index();
});

function index(){
    document.querySelector('#buttons').style.display = 'block';


}

function alunos(title){
    document.querySelector('#div_alunos').style.display = 'block';
    document.querySelector('#buttons').style.display = 'none';

}

function add_aluno(title){

    document.querySelector('#add').style.display = 'block';
    document.querySelector('#buttons').style.display = 'none';



}

function atualiza(title){
    document.querySelector('#edit').style.display = 'block';
    document.querySelector('#buttons').style.display = 'none';

}

function deleta(title){
    document.querySelector('#del').style.display = 'block';
    document.querySelector('#buttons').style.display = 'none';


}
// alunos

function show_pc(){
    document.querySelector('#pc').style.display = 'block';
}

