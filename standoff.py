import requests

def account(id: str):
    headers = {
    'Accept': '*/*',
    'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'Connection': 'keep-alive',
    'Content-Type': 'application/json',
    # 'Cookie': 'Option_AB_v5=Option_A; _ym_uid=1684659818168046438; _ym_d=1684659818; _ym_visorc=w; _ym_isad=1',
    'Referer': 'https://store.standoff2.com/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
    'YandexClientId': '2184659818168046438',
    'rctoken': '13AL8dmw-tDFJlhhwPzJUpn2SjaNmug80tZtH9i8RndvqHY7OjkCDSgF7ninb4BRBBPZgxMVCeQhYbbXAUbL0pqHn79Rznx5IFbAR3s5FSVYKjhUdXGrvYvjPGdgiyk6pdC_owd3hHiC-Y8BEElaA6r7VyDS68-vtgSxtjwOqICkvJe9L6w3orvacp2TM_d3QPcbkC3nrDEXYtymhh2LNf814qmk_ymZpPKDb7dTtPDnid-84RbEjTstbkKcElifOzUv5heHLYdSr7-K8zclSB98FJ92QPbbFn0ZTUGsp2SRGvep_JPFqOfrSOsOdvahpCVF_w35e9mZWqjfP_tP2ofoseJJzHslLFNJG5_fPwMTqp3FDBWF9yfIpN3Kmy8lFWU-ZTyZsrbyELNfkzIdMIwQKzvC2W6Qx_LboqO9B_fGCGIH9UHXnnmoZ-GKn-a3Nhl3mCux_n65wDaBf-d019ZKlEJg8WplMANy-vXuGd_qXFPSonZesOl7rC3GyT_MtITFWjYTytfInVhg8CIabU-YnHtWLF-3a2ZbOWj5wUGIiyQiDi_Jd5yHRN04x8ZhA4th7ip6O7oTpTydxuBxAGgfughbnk3935YwZP09DTRxYxqhQhuaxF6BIe_I__ooqAqGThcVzQDUoBZd0jEJXRlCkewjGjO3UZyK5NYMPwqxeY0uwSPGqZT8h4f5n56HQ4Dve9CtNan_br-27NtrCm2YgXE6gWQ5r1zR-ebyaTcefe5VxSRhtOpadY7ha14PiKhouUKixa7OxhAoaHF-hU5J35B1LVEr7BIYnt2GyQmAHScdwx60bkQ3GUQ0taET-V5vp2okZ0Cw3ezJqh31fXZhTFlBw_86sJzIAkFwi9c3YpwUa2V7n6zNxjzWfm3b8LTNLgAUoHgV7oXhTO_fCPxFr1ttsQYZRHceK3LEY3n97VP2pNscN7yh_P4_OMY0ihZen09RkURKNKAVPtR2NOv72feGkh9g5pokFDxANNS1K5R0QV4i_AKrvHevq3BVhCWyg1upv2mpU4BbDM7ohNl7VVWkI8DfvxFZFSKoo1IxFc2ysDG-34XInECv1JXAEj2F4rKkzaQwDIQGWGfD5mfktfrG9M8izbPZFuGa098WCuCPl64AghakK4ZdFi9qBT5JCmog-9jPpGLPq2fBsIJVP8Sqiz0BOBjRgSPJ6ju4M79Uw61YVz2DXbPxDVg5kvO84v4uriSvfcP5qv4UBB_k7_fvTrE8joVLVXuI_jtuLkAca2V6cQzDDZ2XRk8CFNUSHBWMt9T-TtDFlhbbuzmzgcl7IRyFiyYgjBnxTn4AW7BxluXoTJM9VOfCo7qIdGuB9O55TfU5EwZHLw68LbolwLdQ_Fee2vPJzdzO4Pq6xvtE0QOwoxNfcZw4CoobY3YRMbeZzIZP8zaC78SivBR5DcuD3lpNtzNdEHvdDgmdmOw3DHa45xPfE',
    'sec-ch-ua': '"Google Chrome";v="113", "Chromium";v="113", "Not-A.Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    }
    response = requests.get('https://store.standoff2.com/api/v1/accounts/43123341', headers=headers).json()
    return response['name'], response['avatar']
def avatar(url: str):
    f=open(r'gg.webp', "wb")
    ufr = requests.get(url)
    f.write(ufr.content)
    f.close()
