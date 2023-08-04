frappe.ui.form.on('Material Request', {
	refresh: function(frm) {
        // Hide the print button
        // var printButton = document.querySelector('[data-original-title="Print"]');
        // if (printButton) {
        //     printButton.style.display = 'none';
        // }

		// frm.add_custom_button('<i class="fa fa-file-text-o"></i> Print', function () {
		// 	console.log(frappe.urllib.get_full_url("/printview?"));
		// 	let w = window.open(
		// 		frappe.urllib.get_full_url(
		// 			"/printview?doctype=" +
		// 			encodeURIComponent("Material Request") +
		// 			"&name=" +
		// 			encodeURIComponent(frm.doc.name) +
		// 			"&trigger_print=1" +
		// 			"&format=" +
		// 			encodeURIComponent("dggdcg") +
		// 			"&no_letterhead=" +
		// 			("1") +
		// 			"&letterhead=" +
		// 			encodeURIComponent("No") +
		// 			("&_lang=en")
		// 		)
		// 	);
		// })
    }
});