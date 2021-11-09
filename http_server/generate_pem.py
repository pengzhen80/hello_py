# import OpenSSL
# from OpenSSL._util import lib as _lib, ffi as _ffi
# from OpenSSL.crypto import _new_mem_buf, _bio_to_string

# bio_pub = _new_mem_buf()  # Memory buffers to write to
# bio_priv = _new_mem_buf()

# helper = OpenSSL.crypto._PassphraseHelper(OpenSSL.crypto.FILETYPE_PEM, None)

# pk = OpenSSL.crypto.PKey()
# pk.generate_key(OpenSSL.crypto.TYPE_RSA, 2048)

# # Convert from EVP_PKEY type to RSA type
# rsa_pkey = _lib.EVP_PKEY_get1_RSA(pk._pkey)


# result_code = _lib.PEM_write_bio_RSAPublicKey(bio_pub, rsa_pkey)
# result_code = _lib.PEM_write_bio_RSAPrivateKey(
#     bio_priv, rsa_pkey, _ffi.NULL, _ffi.NULL, 0,
#     helper.callback, helper.callback_args)

# print(_bio_to_string(bio_pub))
# print(_bio_to_string(bio_priv))


############ key
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa

key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048,
)
# Write our key to disk for safe keeping
with open("key.pem", "wb") as f:
    f.write(key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.TraditionalOpenSSL,
        encryption_algorithm=serialization.BestAvailableEncryption(
            b"passphrase"),
    ))


############# cert
from cryptography import x509
from cryptography.x509.oid import NameOID
from cryptography.hazmat.primitives import hashes
# Generate a CSR
csr = x509.CertificateSigningRequestBuilder().subject_name(x509.Name([
    # Provide various details about who we are.
    x509.NameAttribute(NameOID.COUNTRY_NAME, u"US"),
    x509.NameAttribute(NameOID.STATE_OR_PROVINCE_NAME, u"California"),
    x509.NameAttribute(NameOID.LOCALITY_NAME, u"San Francisco"),
    x509.NameAttribute(NameOID.ORGANIZATION_NAME, u"My Company"),
    x509.NameAttribute(NameOID.COMMON_NAME, u"mysite.com"),
])).add_extension(
    x509.SubjectAlternativeName([
        # Describe what sites we want this certificate for.
        x509.DNSName(u"mysite.com"),
        x509.DNSName(u"www.mysite.com"),
        x509.DNSName(u"subdomain.mysite.com"),
    ]),
    critical=False,
    # Sign the CSR with our private key.
).sign(key, hashes.SHA256())
# Write our CSR out to disk.
with open("csr.pem", "wb") as f:
    f.write(csr.public_bytes(serialization.Encoding.PEM))
