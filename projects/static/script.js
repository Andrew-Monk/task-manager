<script>
    const buttons = document.querySelectorAll('.base-nav-button');
    buttons.forEach(function(button) {
        button.addEventListener('mousedown', function() {
            this.style.boxShadow = 'none';
        });
        button.addEventListener('mouseup', function() {
            this.style.boxShadow = '0px 5px 0px 0px #ff8c00';
        });
    });
</script>
