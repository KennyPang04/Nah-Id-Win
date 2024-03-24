function main() {
    document.addEventListener('DOMContentLoaded', function() {
        var paragraph = document.getElementById('js_test');
        
        if (paragraph) {
            paragraph.textContent = 'This text is added using JavaScript! Press the blue + to make a post';
        }
      
    });
}

main()
