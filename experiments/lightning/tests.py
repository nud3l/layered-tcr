from extract_closing import query_blockstream_api
import json


def test_blockstream_output_query():
    tx_hash = "fb633bca751bca5250e87e345f9006c6eb0964bc9d6660b4212b38718041323e"
    tx = query_blockstream_api(tx_hash, "0")
    response = "{'spent': True, 'txid': '9bf15bf03b3503afeedca6ce43240d030e9d55b20b7a8312e8777e4ff8839d74', 'vin': 0, 'status': {'confirmed': True, 'block_height': 557681, 'block_hash': '0000000000000000002d7bac436f62fea30d8160d9b714303c9d1bbd08d052c3', 'block_time': 1546994351}}"
    assert (tx == json.loads(response))


def test_blockstream_tx_query():
    tx_out_hash = "9bf15bf03b3503afeedca6ce43240d030e9d55b20b7a8312e8777e4ff8839d74"
    tx_out = query_blockstream_api(tx_out_hash)
    response = "{'txid': '9bf15bf03b3503afeedca6ce43240d030e9d55b20b7a8312e8777e4ff8839d74', 'version': 2, 'locktime': 548665118, 'vin': [{'txid': 'fb633bca751bca5250e87e345f9006c6eb0964bc9d6660b4212b38718041323e', 'vout': 0, 'prevout': {'scriptpubkey': '00208a5b02370ae85bf6bf62559d89a163b22ebc44192b52dc644af9edecdc69f574', 'scriptpubkey_asm': 'OP_0 OP_PUSHBYTES_32 8a5b02370ae85bf6bf62559d89a163b22ebc44192b52dc644af9edecdc69f574', 'scriptpubkey_address': 'bc1q3fdsydc2apdld0mz2kwcngtrkghtc3qe9dfdcez2l8k7ehrf746q87umf0', 'scriptpubkey_type': 'v0_p2wsh', 'value': 500000}, 'scriptsig': '', 'scriptsig_asm': '', 'witness': ['', '304402201c71878453b03b46077eb386807532cddc80905182c03de5b995dcefd3e19d38022061425c6afa33049771a4d31f024e9e346b46c88d83853ba086cefae43a44d16601', '304402200ff827ab340fc1b8b98ddc0652ce1d8a07f28d9f3c65de99483403420c35ee7f022035854d76c5fe367568b80294f40a1e5949812558ef9489b4908b77ea0601d2cf01', '5221020f1a4898a090b3351ffab18cbbacfba8ae586069b7bb9983d559d060b9b3b8f02103523a0970ecc737544f2005e5abee9ce15a7c8eabb6494b9970a142ff477a3a1b52ae'], 'is_coinbase': False, 'sequence': 2153472071}], 'vout': [{'scriptpubkey': '00149044020efcbdbb63f3d8c2a2373400a82a5e4c53', 'scriptpubkey_asm': 'OP_0 OP_PUSHBYTES_20 9044020efcbdbb63f3d8c2a2373400a82a5e4c53', 'scriptpubkey_address': 'bc1qjpzqyrhuhkak8u7cc23rwdqq4q49unzna5hmyf', 'scriptpubkey_type': 'v0_p2wpkh', 'value': 1120}, {'scriptpubkey': '002068d1cbde2b902a049c60b9285d40901162b66809b1f9b970982977a46b1f25f6', 'scriptpubkey_asm': 'OP_0 OP_PUSHBYTES_32 68d1cbde2b902a049c60b9285d40901162b66809b1f9b970982977a46b1f25f6', 'scriptpubkey_address': 'bc1qdrguhh3tjq4qf8rqhy596sysz93tv6qfk8umjuyc99m6g6clyhmqweppgs', 'scriptpubkey_type': 'v0_p2wsh', 'value': 498308}], 'size': 345, 'weight': 720, 'fee': 572, 'status': {'confirmed': True, 'block_height': 557681, 'block_hash': '0000000000000000002d7bac436f62fea30d8160d9b714303c9d1bbd08d052c3', 'block_time': 1546994351}}"
    assert (tx_out == json.loads(response))
