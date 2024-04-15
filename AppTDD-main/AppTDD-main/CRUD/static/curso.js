document.addEventListener('DOMContentLoaded', ()=>{
    document.querySelector('#edit').addEventListener('click', () => editar());
 

    index();
});
function editar(){
    document.querySelector('#editar').style.display = 'block';
    document.querySelector('#conteudo').style.display = 'none';
    document.querySelector('forms').onsubmit() = () =>{
        alert("Mudanças efetuadas com sucesso");
        index();
    };

}
function index(){
    document.querySelector('#editar').style.display = 'none';
    document.querySelector('#conteudo').style.display = 'block';
}