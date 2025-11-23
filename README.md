

## Projenin Amacı

Bu demo ile;

✔ GitHub Actions ile Docker image’ın otomatik olarak build edilmesi  
✔ Her push işleminde yeni image tag üretilmesi  
✔ Helm `values.yaml` içindeki imaj tag bilgisinin CI tarafından güncellenmesi  
✔ ArgoCD’nin manifests branch’ini izleyerek otomatik deploy yapması  
✔ Kubernetes üzerinde version-rollout ve rollback yönetimi  

amaçlanmıştır.

---

## Genel Mimari Akışı

Developer → Push (main)
↓
GitHub Actions (CI)
↓
Build & Push Docker Image
↓
Manifest branch update (image tag)
↓
Argo CD (CD)
↓
Kubernetes → Automatic Deployment


---

## 📁 Repository Yapısı

├── app/                 # FastAPI uygulaması
│   ├── main.py
│   └── requirements.txt
├── helm/                # Helm Chart (deployment, service, values.yaml)
├── .github/workflows/   # GitHub Actions CI pipeline
│   └── ci-cd.yaml
└── manifests branch     # ArgoCD’nin izlediği branch

## Lokal Geliştirme

```bash
pip install -r app/requirements.txt
python app/main.py
pytest  


kubectl create ns argocd
kubectl apply -n argocd -f https://raw.githubusercontent.com/argoproj/argo-cd/stable/manifests/install.yaml
kubectl -n argocd port-forward svc/argocd-server 8080:443


kubectl -n argocd get secret argocd-initial-admin-secret \
  -o jsonpath="{.data.password}" | base64 -d


  kubectl create ns demo


  kubectl -n demo port-forward svc/demoapp 8081:80
# http://localhost:8081


kubectl run curl-test --image=curlimages/curl --rm -it --restart=Never -- curl demoapp