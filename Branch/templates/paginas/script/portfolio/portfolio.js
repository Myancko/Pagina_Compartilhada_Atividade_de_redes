$(document).ready(function(){
    $(window).scroll(function(){
        if(this.scrollY > 20){
            $('.navbar').addClass("sticky");
        }else{
            $('.navbar').removeClass("sticky");
        }
        if(this.scrollY > 500){
            $('.scroll-up-btn').addClass("show");
        }else{
            $('.scroll-up-btn').removeClass("show");
        }
    });
     $('.scroll-up-btn').click(function(){
         $('html').animate({scrollTop: 0});
     });
     var typed = new Typed(".typing", {
         strings:["Usando ferramentas Python","Usando ferramentas C/C++", "Usando ferramentas HTML/CSS/JS","Usando conhecimento em Machine Learning","Usando conhecimento em Deep Learning", "Usando conhecimento em UX/UI",],
         typeSpeed:100,
         backSpeed:60,
         loop:true
     });
     var typed = new Typed(".typing-2", {
        strings:[ "da Faculdade de ADS", "Integrante da Webminar", "Desenvolvedor!!!",],
        typeSpeed:100,
        backSpeed:60,
        loop:true
    });

    $('.menu-btn').click(function(){
        $('.navbar .menu').toggleClass("active");
        $('.menu-btn i').toggleClass("active");
    });
});