
gsap.registerPlugin(ScrollTrigger)



gsap.to(".test-1", {
    scrollTrigger: {
        trigger: ".customers",
        start: "top bottom",
    },
    x: 100,
    duration: 1.4
});
gsap.to(".test-2", {
    scrollTrigger: {
        trigger: ".customers",
        start: "top bottom",
    },
    x: 200,
    duration: 1.4
});
gsap.to(".test-3", {
    scrollTrigger: {
        trigger: ".customers",
        start: "top bottom",
    },
    x: 300,
    duration: 1.4
});

gsap.to(".card", {
    scrollTrigger: ".card",
    x: -950,
    duration: 3,
});
gsap.to("nav", {
    scrollTrigger: "nav",
    y: 120,
    duration: 2,
});
gsap.to("#img", {
    scrollTrigger: "#img",
    x: -950,
    duration: 3,
});
gsap.to(".search", {
    scrollTrigger: ".search",
    y: -90,
    duration: 2,
});

gsap.to(".car", {
    scrollTrigger: ".car",
    x: 950,
    duration: 3,
});

gsap.to(".light1", {
    opacity: .4, 
    duration: 3, 
    delay: 1
});
gsap.to(".light2", {
    opacity: .4, 
    duration: 3, 
    delay: 1 
});


