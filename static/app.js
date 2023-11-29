function scrollToElement(id) {  
    var element = document.getElementById(id);
    element.scrollIntoView({ behavior: "smooth" });
  }
  
function next_button() {
  const pizd = document.getElementById("slider");
  pizd.scrollLeft += 300; 
}

function previous_button() {
  const pizd = document.getElementById("slider");
  pizd.scrollLeft -= 300;
}

let scrollposition = 0
window.addEventListener("scroll", function() {
  var header = document.getElementById('stickyHeader');
  
  if (window.scrollY > scrollposition) {
    header.classList.remove('sticky');
  }else if(window.scrollY < scrollposition || window.scrollY == 0){
    header.classList.add('sticky');
  }
  scrollposition = this.window.scrollY
});

function child_windows_active() {
  var child_window = document.querySelector(".child_window")
  child_window.classList.remove("disabled")
}

function child_windows_deactive() {
  var child_window = document.querySelector(".child_window")
  child_window.classList.add("disabled")
}

document.querySelector('header ul button').addEventListener('click', function() {
  let allli = document.querySelectorAll('header ul li')
  allli.forEach(function(li) {
    if (li.classList == "active") {
      li.classList.remove("active")
    }else{
      li.classList.add("active")
    }
  })
});

