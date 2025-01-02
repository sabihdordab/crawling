document.addEventListener("DOMContentLoaded", function() {
    document.querySelectorAll('.extra-fields').forEach(function(el) {
        el.style.display = 'none';
    });

    const scraperField = document.querySelector('select[name="scraper"]');
    
    
    function toggleFields() {
        const selectedScraper = scraperField.value;

        
        document.querySelectorAll('.extra-fields').forEach(function(el) {
            el.style.display = 'none';
        });

        if (selectedScraper === 'divar') {
            document.getElementById('divar-fields').style.display = 'block';
        } else if (selectedScraper === 'basalam') {
            document.getElementById('basalam-fields').style.display = 'block';
        } else if (selectedScraper === 'bamilo') {
            document.getElementById('bamilo-fields').style.display = 'block';
        }
    }

    
    scraperField.addEventListener('change', toggleFields);

    
    toggleFields();
});
