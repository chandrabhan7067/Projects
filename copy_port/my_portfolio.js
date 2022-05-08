// console.log('hello')
document.querySelector('.crossburger').style.display = 'none';

document.querySelector('.burger').addEventListener("click",() =>{
    document.querySelector('.menu').classList.toggle('menu-go');

    if (document.querySelector('.menu').classList.contains('menu-go')) {
        document.querySelector('.hamburger').style.display = 'inline';        
        document.querySelector('.crossburger').style.display = 'none';  
    }
    
    else{
        document.querySelector('.hamburger').style.display = 'none'; 
        setTimeout(() => {
            
            document.querySelector('.crossburger').style.display = 'inline';  
        }, 300);       
    }
})