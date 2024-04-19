document.addEventListener('DOMContentLoaded', ()=>{
    document.querySelector('#editar').addEventListener('click', () => editar());
 

    index();
});
function editar(){
    document.querySelector('#edit_al').style.display = 'block';
    document.querySelector('#content').style.display = 'none';
    document.querySelector('forms').onsubmit() = () =>{
        alert("Mudanças efetuadas com sucesso");
        index();
    };

}
function index(){
    document.querySelector('#edit_al').style.display = 'none';
    document.querySelector('#content').style.display = 'block';
}