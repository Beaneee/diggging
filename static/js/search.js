// search input
const searchField =document.querySelector('#search_input');
const searchContainer = document.querySelector('.search_container');

searchField.addEventListener('keyup', (e) => {
    const searchValue = e.target.value;

    if(searchValue.trim().length > 0) {
        console.log('searchValue', searchValue);

        fetch('/posts/search_input/', {
            body: JSON.stringify({text:searchValue}),
            method: "POST",
            headers : { 
                'Content-Type': 'application/json',
                'Accept': 'application/json'
            },
        })
            .then((res) => res.json())
            .then((data) => {
            console.log(data)
            if (data.length === 0){
                searchContainer.innerHTML = "검색어와 맞는 글이 없어요"
            } else {
                const txt = data.map(post => {
                    return  `
                        ${post.title}
                        ${post.desc}
                    `
                })
                searchContainer.innerHTML = txt;
            }
            })
    } else {

        searchContainer.innerHTML = "검색해주셈"
    }
})


const language = document.getElementById('id_field');
const os = document.getElementById('id_field2');
const problem_solving = document.getElementById('id_field3');
const framework = document.getElementById('id_field4');

const select = document.getElementById('select');

select.addEventListener('change', () => {
    const langValue = language.options[language.selectedIndex].value;
    const osValue = os.options[os.selectedIndex].value;
    const solveValue = problem_solving.options[problem_solving.selectedIndex].value;
    const frameValue = framework.options[framework.selectedIndex].value;

    fetch('/posts/search_select/', {
        body: JSON.stringify({language:langValue ,os:osValue,
                            problem_solving:solveValue, framework:frameValue}),
        method: "POST",
        headers : { 
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        },
    })
    .then(res => res.json())
    .then(data => {
        console.log(data)                
        
        if (data.length === 0){
            searchContainer.innerHTML = "검색어와 맞는 글이 없어요"
        } else {
            const txt = data.map(post => {
                return  `
                    ${post.title}
                `
            })
            searchContainer.innerHTML = txt;
        }
    })
})