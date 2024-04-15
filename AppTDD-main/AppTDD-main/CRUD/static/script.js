document.addEventListener('DOMContentLoaded', ()=>{
    document.querySelector('#procura_aluno').addEventListener('click', () => procura_aluno('procura aluno'));
    document.querySelector('#add_aluno').addEventListener('click', () => add_aluno('Adiciona alunos'));
    document.querySelector('#update').addEventListener('click', () => atualiza('update'));
    document.querySelector('#delete').addEventListener('click', () => deleta('delete'));
    
    var voltar = document.getElementsByClassName("voltar");
    for (var i = 0; i < voltar.length; i++) {
      voltar[i].addEventListener('click', () => index());
    }

    index();
});

function index(){
    document.querySelector('#buttons').style.display = 'block';
    document.querySelector('#edit').style.display = 'none';
    document.querySelector('#proc').style.display = 'none';
    document.querySelector('#add').style.display = 'none';
    document.querySelector('#del').style.display = 'none';

}

function procura_aluno(title){
    document.querySelector('#buttons').style.display = 'none';
    document.querySelector('#edit').style.display = 'none';
    document.querySelector('#proc').style.display = 'block';
    document.querySelector('#add').style.display = 'none';
    document.querySelector('#del').style.display = 'none';
}

function add_aluno(title){
    document.querySelector('#buttons').style.display = 'none';
    document.querySelector('#edit').style.display = 'none';
    document.querySelector('#add').style.display = 'block';
    document.querySelector('#proc').style.display = 'none';
    document.querySelector('#del').style.display = 'none';


}

function atualiza(title){
    document.querySelector('#buttons').style.display = 'none';
    document.querySelector('#edit').style.display = 'block';
    document.querySelector('#add').style.display = 'none';
    document.querySelector('#proc').style.display = 'none';
    document.querySelector('#del').style.display = 'none';
}

function deleta(title){
    document.querySelector('#buttons').style.display = 'none';
    document.querySelector('#edit').style.display = 'none';
    document.querySelector('#add').style.display = 'none';
    document.querySelector('#proc').style.display = 'none';
    document.querySelector('#del').style.display = 'block';

}