import { Button } from "@/components/ui/button";
import { Card, CardContent } from "@/components/ui/card";
import { Section } from "@/components/ui/section";
import { useNavigate } from "react-router-dom";
import ContactForm from "@/components/ContactForm";
import Timeline from "@/components/Timeline";
import MediaSection from "@/components/MediaSection";
import BusinessVisionSection from "@/components/BusinessVisionSection";
import {
  Building2,
  Calculator,
  Scale,
  Users,
  Shield,
  TrendingUp,
  CheckCircle,
  ArrowRight,
  MessageSquare,
  Handshake,
  FileText,
  Briefcase,
  Globe,
  Gavel,
  UserCheck,
  BrainCircuit
} from "lucide-react";
import legalImage from "@/assets/legal-concept.jpg";
import HeroCarousel from "@/components/HeroCarousel";

const Home = () => {
  const navigate = useNavigate();
  const practiceAreas = [
    {
      icon: Building2,
      title: "Societário",
      description: "Elaboração e assessoria de documentos societários, mediação de conflitos entre sócios, e atuação judicial para ruptura de sociedades.",
      color: "text-accent"
    },
    {
      icon: Briefcase,
      title: "Fusões e Aquisições (M&A)",
      description: "Suporte especializado na compra, venda, fusão e incorporação de empresas.",
      color: "text-red-accent"
    },
    {
      icon: BrainCircuit,
      title: "Reestruturação Societária",
      description: "Apoio em reestruturações corporativas e crises financeiras, incluindo reorganizações societárias e sucessão familiar.",
      color: "text-accent"
    },
    {
      icon: Calculator,
      title: "Tributário",
      description: "Consultoria na interpretação e aplicação de normas tributárias federais, estaduais e municipais, abrangendo análise estratégica com eventual condução de ações judiciais de natureza tributária e previdenciária.",
      color: "text-red-accent"
    },
    {
      icon: FileText,
      title: "Contratos",
      description: "Assessoramento e representação em todas as etapas dos processos de negociação e gestão de contratos, incluindo atuação integral em caráter pós-contratual.",
      color: "text-accent"
    },
    {
      icon: Scale,
      title: "Contencioso Cível",
      description: "Atuação estratégica em questões cíveis, comerciais, bancárias, de recuperação de crédito, reestruturação de dívida, falência e responsabilidade civil.",
      color: "text-red-accent"
    },
    {
      icon: UserCheck,
      title: "Contencioso Trabalhista",
      description: "Assessoria jurídica preventiva para recursos humanos, representação em negociações e gerenciamento de conflitos trabalhistas.",
      color: "text-accent"
    },
    {
      icon: Handshake,
      title: "Arbitragem e Mediação",
      description: "Representação em procedimentos arbitrais e mediação de disputas contratuais, societárias, de consumo, relações de trabalho e outras.",
      color: "text-red-accent"
    }
  ];

  const differentials = [
    {
      icon: Handshake,
      title: "Senior Hands On",
      description: "Apostamos no efetivo envolvimento dos sócios nos negócios confiados a nós."
    },
    {
      icon: TrendingUp,
      title: "Descomplicamos o Complexo",
      description: "Atuamos nas mais complexas e sofisticadas operações do mercado buscando descomplificar os temas jurídicos e facilitar a tomada de decisões por nossos clientes."
    },
    {
      icon: Shield,
      title: "Qualidade como Premissa",
      description: "Qualidade é a premissa de tudo o que fazemos, mas queremos ainda mais. Visamos ser decisivos no sucesso dos nossos clientes."
    },
    {
      icon: Globe,
      title: "Criatividade e Inovação",
      description: "Dividimos conhecimento com o cliente e entendemos seus interesses e necessidades, vendo além dos problemas para encontrar soluções."
    }
  ];

  const recentArticles = [
    {
      id: 1,
      title: "Cresce incidência de processos coletivos",
      excerpt: "Treinamentos jurídicos podem evitar essa modalidade de ação que tem movimentado os tribunais brasileiros.",
      date: "15 Jan 2024",
      category: "Contencioso"
    },
    {
      id: 2,
      title: "Justiça do RS condena trabalhador a pagar indenização a empresa",
      excerpt: "Mayra Palópoli comenta decisão pioneira que estabelece responsabilidade civil do ex-funcionário perante a empresa.",
      date: "12 Jan 2024",
      category: "Trabalhista"
    },
    {
      id: 3,
      title: "Arbitragem ganha força no Estado",
      excerpt: "Nova câmara para atender pequenas empresas deve abrir em dois meses. Mayra Palópoli analisa as tendências do setor.",
      date: "10 Abr 2011",
      category: "Empresarial"
    }
  ];

  return (
    <div className="min-h-screen">
      {/* Hero Section with Carousel */}
      <HeroCarousel />

      {/* Practice Areas */}
      <Section variant="muted" className="relative">
        <div className="absolute top-0 left-8 w-1 h-16 bg-accent"></div>
        <div className="pl-16">
          <div className="mb-16">
            <div className="flex items-center space-x-4 mb-6">
              <div className="w-2 h-2 bg-accent rounded-full"></div>
              <span className="text-sm font-medium text-accent uppercase tracking-wider">Especialidades</span>
            </div>
            <h2 className="text-3xl md:text-4xl font-heading font-bold text-foreground mb-4">
              Áreas de Atuação
            </h2>
            <p className="text-xl text-muted-foreground max-w-2xl">
              Soluções jurídicas especializadas para os principais desafios empresariais
            </p>
          </div>
        </div>

        <div className="pl-16">
          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
            {practiceAreas.map((area, index) => (
              <Card key={index} className="wine-card hover:shadow-elegant transition-all duration-300 group border-l-4 border-l-transparent hover:border-l-accent">
                <CardContent className="p-5">
                  <div className="flex items-start space-x-3">
                    <div className="flex-shrink-0">
                      <area.icon className={`h-8 w-8 ${area.color} group-hover:scale-110 transition-transform duration-300`} />
                    </div>
                    <div className="flex-1 min-w-0">
                      <h3 className="text-base font-heading font-semibold mb-2 text-foreground">
                        {area.title}
                      </h3>
                      <p className="text-muted-foreground leading-relaxed mb-3 text-xs">
                        {area.description}
                      </p>
                      <Button variant="ghost" size="sm" className="text-accent hover:text-accent-foreground hover:bg-accent p-0 text-xs">
                        Saiba Mais
                        <ArrowRight className="h-3 w-3 ml-1" />
                      </Button>
                    </div>
                  </div>
                </CardContent>
              </Card>
            ))}
          </div>
        </div>
      </Section>

      {/* Business Vision Section */}
      <BusinessVisionSection />

      {/* Stats Section */}
      <Section className="relative">
        <div className="absolute top-0 left-4 sm:left-8 w-1 h-16 bg-accent"></div>
        <div className="pl-8 sm:pl-16">
          <div className="grid grid-cols-2 md:grid-cols-4 gap-4 sm:gap-8">
            <div className="text-center">
              <div className="text-2xl sm:text-3xl md:text-4xl font-heading font-bold text-accent mb-2">20+</div>
              <p className="text-xs sm:text-sm text-muted-foreground font-medium">Anos de Experiência</p>
            </div>
            <div className="text-center">
              <div className="text-2xl sm:text-3xl md:text-4xl font-heading font-bold text-accent mb-2">500+</div>
              <p className="text-xs sm:text-sm text-muted-foreground font-medium">Clientes Atendidos</p>
            </div>
            <div className="text-center">
              <div className="text-2xl sm:text-3xl md:text-4xl font-heading font-bold text-accent mb-2">1000+</div>
              <p className="text-xs sm:text-sm text-muted-foreground font-medium">Casos Resolvidos</p>
            </div>
            <div className="text-center">
              <div className="text-2xl sm:text-3xl md:text-4xl font-heading font-bold text-accent mb-2">8</div>
              <p className="text-xs sm:text-sm text-muted-foreground font-medium">Áreas de Especialização</p>
            </div>
          </div>
        </div>
      </Section>

      {/* Timeline */}
      <Section variant="muted">
        <Timeline />
      </Section>

      {/* Expansion Section */}
      <Section>
        <div className="text-center mb-12">
          <h2 className="text-3xl md:text-4xl font-heading font-bold text-foreground mb-6">
            Expansão Estratégica com Presença Nacional e Internacional
          </h2>
          <p className="text-xl text-muted-foreground max-w-4xl mx-auto leading-relaxed mb-8">
            Atuamos com infraestrutura própria diretamente em São Paulo, o principal centro econômico do Brasil,
            e através de escritórios parceiros em todo o país e no exterior, escolhidos pela tradição,
            confiabilidade e competência.
          </p>
          <div className="bg-white p-8 rounded-lg shadow-card max-w-2xl mx-auto">
            <p className="text-lg text-muted-foreground leading-relaxed italic">
              "O escritório atua no campo empresarial em todos os graus de jurisdição, administrativa ou
              judicial, consultiva e contenciosa, apresentando ideias inovadoras para a resolução de litígios,
              além, principalmente, da prevenção e visão antecipada deles."
            </p>
          </div>
        </div>
      </Section>

      {/* Media Section */}
      <MediaSection />

      {/* Recent Articles */}
      <Section className="relative">
        <div className="absolute top-0 left-8 w-1 h-16 bg-accent"></div>
        <div className="pl-16">
          <div className="mb-16">
            <div className="flex items-center space-x-4 mb-6">
              <div className="w-2 h-2 bg-accent rounded-full"></div>
              <span className="text-sm font-medium text-accent uppercase tracking-wider">Conhecimento</span>
            </div>
            <h2 className="text-3xl md:text-4xl font-heading font-bold text-foreground mb-4">
              Insights Jurídicos
            </h2>
            <p className="text-xl text-muted-foreground max-w-2xl">
              Mantenha-se informado sobre as principais mudanças no cenário jurídico empresarial
            </p>
          </div>
        </div>

        <div className="pl-16">
          <div className="grid grid-cols-1 md:grid-cols-3 gap-8">
            {recentArticles.map((article, index) => (
              <Card key={index} className="wine-card hover:shadow-elegant transition-all duration-300 group border-l-4 border-l-transparent hover:border-l-accent">
                <CardContent className="p-6">
                  <div className="mb-4">
                    <span className="inline-block px-3 py-1 bg-accent/10 text-accent text-sm font-medium rounded-full">
                      {article.category}
                    </span>
                  </div>
                  <h3 className="text-xl font-heading font-semibold text-foreground mb-3 group-hover:text-accent transition-colors">
                    {article.title}
                  </h3>
                  <p className="text-muted-foreground mb-4 leading-relaxed">
                    {article.excerpt}
                  </p>
                  <div className="flex items-center justify-between">
                    <span className="text-sm text-muted-foreground">{article.date}</span>
                    <Button
                      variant="ghost"
                      size="sm"
                      className="text-accent hover:text-accent-foreground hover:bg-accent p-0"
                      onClick={() => navigate(`/blog/${article.id}`)}
                    >
                      Ler mais
                      <ArrowRight className="h-4 w-4 ml-1" />
                    </Button>
                  </div>
                </CardContent>
              </Card>
            ))}
          </div>

          <div className="text-center mt-12">
            <Button
              variant="outline"
              size="lg"
              className="border-accent text-accent hover:bg-accent hover:text-accent-foreground"
              onClick={() => navigate('/blog')}
            >
              Ver Todos os Artigos
              <ArrowRight className="h-5 w-5 ml-2" />
            </Button>
          </div>
        </div>
      </Section>

      {/* CTA Section */}
      <Section variant="wine">
        <div className="text-center">
          <h2 className="text-3xl md:text-4xl font-heading font-bold text-primary-foreground mb-6">
            Pronto para Crescer com Segurança Jurídica?
          </h2>
          <p className="text-xl text-primary-foreground/80 mb-8 max-w-2xl mx-auto">
            Entre em contato conosco e descubra como podemos ajudar sua empresa a alcançar seus objetivos com total segurança jurídica.
          </p>
          <Button size="lg" className="bg-accent hover:bg-accent/90 text-accent-foreground font-semibold px-8 py-4 text-lg">
            <MessageSquare className="h-5 w-5 mr-2" />
            Agendar Consulta
          </Button>
        </div>
      </Section>
    </div>
  );
};

export default Home;

