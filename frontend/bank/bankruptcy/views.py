from django.shortcuts import render, HttpResponse
import joblib, pickle, numpy

model = joblib.load('static/bankruptcy predictor')
m = pickle.load(open('static/bankruptcy_predictor.pkl', 'rb'))

# Create your views here.
def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def prediction(request):
    if request.method == 'POST':
        #operating prfit rate
        opr = float(request.POST.get('opr'))
        #operating expense rate
        oer = float(request.POST.get('oer'))
        #revenue per share
        rps = float(request.POST.get('rps'))
        #Interest-Bearing debt interest rate
        ibdir = float(request.POST.get('ibdir'))
        #Realized Sales Gross Profit Growth Rate
        rsgpgr = float(request.POST.get('rsgpgr'))
        #operating profit growth rate
        opgr = float(request.POST.get('opgr'))
        #continouos net profit growth rate
        cnpgr = float(request.POST.get('cnpgr'))
        #current ratio
        cr = float(request.POST.get('cr'))
        #interest expense ratio
        ier = float(request.POST.get('ier'))
        #total debt / total net worth
        tdtnw = float(request.POST.get('tdtnw'))
        #long term fund sustainability ratio
        ltfsr = float(request.POST.get('ltfsr'))
        #Accounts receivable turnover
        art = float(request.POST.get('art'))
        #acerage collection days
        acd = float(request.POST.get('acd'))
        #inventory turnover ate
        itr = float(request.POST.get('itr'))
        #net worth turnover rate
        nwtr = float(request.POST.get('nwtr'))
        #Qucik Assets / Current Liabilities
        qacl = float(request.POST.get('qacl'))
        #Inventory / Working Capital
        iwc = float(request.POST.get('iwc'))
        #Inventory / Current Liabilities
        icl = float(request.POST.get('icl'))
        #Current Liabilities / Liabilities
        cll = float(request.POST.get('cll'))
        #
        ltlca = float(request.POST.get('ltlca'))
        #
        catr = float(request.POST.get('catr'))
        #
        ctr = float(request.POST.get('ctr'))
        #
        nci = float(request.POST.get('nci'))
        #
        dfl = float(request.POST.get('dfl'))
        #
        icrebit = float(request.POST.get('icrebit'))
        #
        nif = float(request.POST.get('icrebit'))

        #production only
        #print(oer, opr, rps, ibdir)

        #acutal prediction
        pred = model.predict_proba([[opr, 
                                          oer, 
                                          rps, 
                                          ibdir, 
                                          rsgpgr, 
                                          opgr, 
                                          cnpgr, 
                                          cr, 
                                          ier, 
                                          tdtnw, 
                                          ltfsr, 
                                          art, 
                                          acd, 
                                          itr, 
                                          nwtr, 
                                          qacl, 
                                          iwc, 
                                          icl, 
                                          cll, 
                                          ltlca,
                                          catr,
                                          ctr,
                                          nci,
                                          dfl,
                                          icrebit,
                                          nif]]
                                          )[:,1]
        
        pred = numpy.ndarray.tolist(pred)

        if pred[0] < 0.5:
            output = {
                'output': pred[0]
            }

        else:
            output = {
                'output': pred[0]
            }

        #production only
        #print(output['output'])

        return render(request, 'prediction.html', output)
    
    else:
        return render(request, 'prediction.html')