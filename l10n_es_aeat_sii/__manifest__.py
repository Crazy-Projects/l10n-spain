# Copyright 2017 Acysos - Ignacio Ibeas <ignacio@acysos.com>
# Copyright 2017 Diagram Software S.L.
# Copyright 2017 MINORISA - <ramon.guiu@minorisa.net>
# Copyright 2017 Studio73 - Pablo Fuentes <pablo@studio73.es>
# Copyright 2017 Studio73 - Jordi Tolsà <jordi@studio73.es>
# Copyright 2017 Factor Libre - Ismael Calvo
# Copyright 2017 Otherway - Pedro Rodríguez Gil
# Copyright 2017-2021 Tecnativa - Pedro M. Baeza
# Copyright 2018 Javi Melendez <javimelex@gmail.com>
# Copyright 2018 Angel Moya <angel.moya@pesol.es>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    "name": "Suministro Inmediato de Información en el IVA",
    "version": "12.0.1.9.0",
    "category": "Accounting & Finance",
    "website": "https://odoospain.odoo.com",
    "author": "Acysos S.L.,"
              "Diagram,"
              "Minorisa,"
              "Studio73,"
              "FactorLibre,"
              "Comunitea,"
              "Otherway,"
              "Tecnativa,"
              "Javi Melendez,"
              "Odoo Community Association (OCA)",
    "license": "AGPL-3",
    "application": False,
    "installable": True,
    "development_status": "Production/Stable",
    "maintainers": [
        'pedrobaeza',
    ],
    "external_dependencies": {
        "python": [
            "zeep",
            "requests",
            "OpenSSL",
        ],
    },
    "depends": [
        "account_invoice_refund_link",
        "l10n_es",
        "l10n_es_aeat",
        "queue_job",
    ],
    "data": [
        "data/ir_config_parameter.xml",
        "data/aeat_sii_tax_agency_data.xml",
        "views/res_company_view.xml",
        "views/account_invoice_view.xml",
        "views/aeat_sii_view.xml",
        "wizards/aeat_sii_password_view.xml",
        "wizards/account_invoice_refund_views.xml",
        "views/aeat_sii_mapping_registration_keys_view.xml",
        "data/aeat_sii_mapping_registration_keys_data.xml",
        "views/aeat_sii_map_view.xml",
        "data/aeat_sii_map_data.xml",
        "security/ir.model.access.csv",
        "security/aeat_sii.xml",
        "views/product_view.xml",
        "views/queue_job_views.xml",
        "views/account_fiscal_position_view.xml",
        "views/res_partner_views.xml",
        "views/aeat_sii_tax_agency_view.xml",
    ],
    "post_init_hook": "add_key_to_existing_invoices",
}
